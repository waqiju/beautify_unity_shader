『缘起和动机』

起初是想为.shader做一个可以格式化代码的插件，设想是用正则表达式加上给token分类就能实现。按照这个思路做下去，发现并没有这么简单。同一个token在不同的上下文中，可能扮演不同的角色，也就对应不同的排版方案。

比如，`;`在CGPROGRAM ... ENDCG中扮演的角色。

```
int a = 10;
for (int i = 0; i <= 10; ++i) { ... }
```

一般而言，`;`代表的是statement的结束，后续接的排版应该是换行。但是在for语句中，分号代表分隔，后续接的是空格。除了类C语言的内容外，像shader中的命令不借助上下文也是很难分隔的。比如，`ColorMask RGB Blend One OneMinusSrcAlpha` 应该在哪里插入回车，哪里插入空格。


『过程概述』

在尝试了一段时间的正则表达式加token分类的方法后，效果不尽人意。便思考用语法分析是不是更有效的方法。（于是，步入深坑）

找个本编译原理的书，就开始“照猫画虎”。按照 (源代码文本) --词法分析--> token_list --语法分析--> syntax_tree，然后遍历syntax_tree，根据syntax_tree的内容来还原代码。

词法分析的工作量和难度较小。过程中纠结多遍的是Number的识别，改了10+遍才改对。像`1.23` `-1e10`这种写法还好，但这种`1.` `.34`这种写法刚开始还真想不到。Number前的`+/-`号的角色判定也需要额外考虑，不是所有数字前面的`+/-`号都是Number的一部分。比如 `a = 1 + 2`，`+/-`号也同样可以作为运算符。

语法分析工作量就加大了很多。了解ll和lr两种语法分析方法，这里shader含有类C语法，应该选用lr分析。和书上的说法一样，一般的编程语言选择的都是符合lr1的语法规则，这里shader大体也是符合的。lr1 parser可以分为两部分，第一部分是根据productions来构造出状态转移关系，第二部分是分析源代码得到syntax_tree。构造主要是用代码实现书上的几个推导方法，和production、nonterminal在代码中如何描述。分析过程就是一个dfm了，production和nonterminal实现好的话，这部分实现就很轻松了。

写出一个能工作的lr1 parser难度还好，但是要写出shader对应的lr1语法的production（或者也叫BNF）要麻烦多了。production要求一是覆盖到所有合法的情况，二是无二义性。覆盖到所有合法情况，这点靠枚举和测试来保证。无二义性在刚开始反而造成了更多的困扰，有些自己写的production，有时怎么看搞不明白在什么情景下会产生二义性。二义性推导多了再加上参考C的grammer，渐渐熟络。

比如，Properties语句block里还有这种写法，`[Enum(UV0, 0, UV1, 1)] _UVSec ("UV Set for secondary textures", Float) = 0`。

最后做下来，感觉第一遍做，总归没有已经精通了的作者在书上讲的那么轻巧。


『开发和测试流程』

整体的代码量还是比较大，使用unittest来推进测试。测试语法分析和格式化代码功能，用的是unity官方公布的builtin目录下的所有*.shader文件。即，目前的两个主要功能，都能通过官方公布的builtin目录下的*.shader文件测试。

一遍完整的lr parser构建流程：

1. 写出production。这块的样例可参考test/combined_test/syntax.txt。

2. 使用syntax_to_py把syntax.txt翻译为python代码。即productions.py和nonterminals.py。

3. 检查和调整生成的productions.py和nonterminals.py。

4. 构建lr的状态转移图。

5. 使用lr parser分析源代码。


『技术细节1：关于预处理语句的折衷处理以及未来的改进点』

在开发过程中，这个曾是绵延不绝的痛苦源头。

最开始想把preprocessor statement当做正常的语句来处理，之后，现实证明走不通。

a. marco_fold可以是任意的语法元素。

eg, `UNITY_VERTEX_OUTPUT_STEREO` 展开后是自带有`;`号的。

b. C条件编译，隔开的可以是任意语法元素。

eg,
```
#ifdef UNITY_HDR_ON
half4
#else
fixed4
#endif
frag (unity_v2f_deferred i) : SV_Target
{
...
}
```

开始想用这种模拟的方法，达到最小代价get work done，后来改着改着逐步陷入泥潭。

正确的处理方法是，独立实现一个preprocessor。于是在lexer和parser之间插入一个preprocessor。不过在目前的实现，preprocessor还是不完整、带有缺陷的。比如，marco应该展开后替换掉原来token，这个没有去实现。比如，有#if时，token_list就不是线性的了，应该是带分支了，这个也没有去实现。


『技术细节2：关于类C语法』

类C语法的CGPROGRAM ... ENDCG也带有了一些问题。

C语言并不是严格的上下文无法语法，所以仅仅依靠lr1的分析，是不能够覆盖C语言的所有语法。

比如，typedef int newInt; newInt a = 10; void print(newInt x) { ... }。这里newInt如果按照正常的流程会被识别为ID，a和x也是ID，按照一般的语法，是没有两个ID之间是空格隔开的，这是非法的。但如果前一ID是type，则又是合法的。（虽然CG里没有typedef，但是struct声明的类型和typedef效果是一样的）。

某个ID到底能不能看做type，这个就和内容相关了。然后也可能会导致某些二义性。比如，y = (newInt) x。（这里存疑下，这个二义性也可能只是当时考虑欠当，以后有时间再来细究吧）。


『技术细节3：代码格式化的功能实现』

正如前面所言，代码格式化是通过遍历syntax_tree来实现。相对于给token分类（且不可行），在syntax_tree上排版要简单、明了多了。

排版主要是缩进、回车、空格三者之间的选择。不过偶尔也会遇到一些头疼的问题，比如，注释。

注释在lexer得到的token_list中是存在的，不过在后续的parser并不需要用到comment，所以在syntax_tree中并不存在comment的位置。或者也可以说，comment可以存在与syntax_tree的任意结点。

找回注释，正确的做法应该是在每个syntax_tree的token附近前后回溯token_list。但是，这里的实现偷了个懒，只在缩进附近前后回溯token_list。好吧，除了偷懒外，个人更偏爱注释独占一行的风格。


『技术细节4：一些特别的风味』

在测试的过程，才发现有些关键字在Unity Shader中是不区分大小写的。

eg:
```
Fallback Off
FallBack Off
Fallback off
FallBack off 
```

上述4个都是合法的。