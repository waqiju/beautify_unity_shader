import re
try:
    from light_syntax_engine import SyntaxEngine
except:
    from .light_syntax_engine import SyntaxEngine


def format(text):
    engine = SyntaxEngine(text)
    engine.add('beginning_of_file', lambda text, pos, context: pos == 0, formatBeginningOfFile)
    engine.add('head_of_line', lambda text, pos, context: context['isHeadOfLine'] == True, formatHeadOfLine)
    engine.add('copy_to_eof', lambda text, pos, context: True, copyToEOF)
    engine.add('literal_string', lambda text, pos, context: text[pos] == r'"', formatLiteralString)
    engine.add('line_comment', lambda text, pos, context: text[pos:pos + 2] == r'//', formatLineComment)
    engine.add('block_comment', lambda text, pos, context: text[pos:pos + 2] == r'/*', formatBlockComment)
    engine.add('char01', matchChar01, formatChar01)
    engine.add('charP1', matchCharP1, formatCharP1)
    engine.add('charN0', matchCharN0, formatCharN0)
    engine.add('left_curly_brace', matchLeftCurlyBrace, formatLeftCurlyBrace)
    engine.add('right_curly_brace', matchRightCurlyBrace, formatRightCurlyBrace)
    engine.add('return_char', matchReturnChar, formatReturnChar)
    engine.add('any_char', lambda text, pos, context: True, formatAnyChar)

    engine.match('beginning_of_file')

    mainFormat(engine)

    return engine.context['formattedText']


def mainFormat(engine):
    while not engine.isEnd():
        if engine.match('head_of_line'):
            continue
        if engine.match('literal_string'):
            continue
        if engine.match('line_comment'):
            continue
        if engine.match('block_comment'):
            continue
        if engine.match('left_curly_brace'):
            continue
        if engine.match('right_curly_brace'):
            continue
        if engine.match('return_char'):
            continue
        if engine.match('char01'):
            continue
        if engine.match('charP1'):
            continue
        if engine.match('charN0'):
            continue
        if engine.match('any_char'):
            continue


def formatBeginningOfFile(text, pos, context):
    context['formattedText'] = ""
    context['indentLevel'] = 0
    context['isHeadOfLine'] = False
    pattern = re.compile(r"\s*")
    match = pattern.match(text, pos)
    if match:
        return match.end()


def copyToEOF(text, pos, context):
    pattern = re.compile(r".*", re.DOTALL)
    match = pattern.match(text, pos)
    if match:
        context['formattedText'] = context['formattedText'] + match.group()
        return match.end()


def formatLiteralString(text, pos, context):
    pattern = re.compile(r'"[^"]*"')
    match = pattern.match(text, pos)
    if match:
        context['formattedText'] = context['formattedText'] + match.group()
        return match.end()


def formatLineComment(text, pos, context):
    pattern = re.compile(r"//.*(?=\n)")
    match = pattern.match(text, pos)
    if match:
        context['formattedText'] = context['formattedText'] + match.group()
        return match.end()


def formatBlockComment(text, pos, context):
    pattern = re.compile(r"/\*.*\*/", re.DOTALL)
    match = pattern.match(text, pos)
    if match:
        context['formattedText'] = context['formattedText'] + match.group()
        return match.end()

r'''
    CharXY charXXiYYY
    0
    1
    P = Plus >=1
    N = Any
    I = Indent
    E = Enter. If refactor, rename it to R
'''

matchChar01 = SyntaxEngine.generateRegexMatcher(r',')


def formatChar01(text, pos, context):
    context['formattedText'] = SyntaxEngine.trimSpaceFromTail(context['formattedText']) \
        + text[pos] \
        + " "

    pattern = re.compile(r"[ \t]*")
    return pattern.match(text, pos+1).end()


matchCharP1 = SyntaxEngine.generateRegexMatcher(r'=|:')


def formatCharP1(text, pos, context):
    context['formattedText'] = context['formattedText'] \
        + (' ' if not context['formattedText'].endswith(' ') else '') \
        + text[pos] \
        + ' '

    pattern = re.compile(r"[ \t]*")
    return pattern.match(text, pos+1).end()



matchCharN0 = SyntaxEngine.generateRegexMatcher(r'[ \t]')


def formatCharN0(text, pos, context):
    pattern = re.compile(r"[ \t]*")
    match = pattern.match(text, pos + 1)
    if match:
        context['formattedText'] = context['formattedText'] + ' '
        return match.end()


# special for {}
def formatChar0EIi0E(text, pos, context):
    context['formattedText'] = SyntaxEngine.trimSpaceReturnFromTail(context['formattedText']) \
        + '\n' \
        + SyntaxEngine.generateIndent(context['indentLevel']) \
        + text[pos] \
        + '\n'
    context['isHeadOfLine'] = True

    pattern = re.compile(r".\s*", re.DOTALL)
    match = pattern.match(text, pos)
    return match.end()


matchLeftCurlyBrace = lambda text, pos, context: text[pos] == '{'


def formatLeftCurlyBrace(text, pos, context):
    rst = formatChar0EIi0E(text, pos, context)
    context['indentLevel'] = context['indentLevel'] + 1
    return rst

# 怎么讲，其实}不是0EIi0E。后面可以接;的
matchRightCurlyBrace = lambda text, pos, context: text[pos] == '}'


def formatRightCurlyBrace(text, pos, context):
    context['indentLevel'] = context['indentLevel'] - 1
    pos = formatChar0EIi0E(text, pos, context)

    pattern = re.compile(r"\s*;")
    match = pattern.match(text, pos)
    if match:
        context['formattedText'] = SyntaxEngine.trimSpaceReturnFromTail(context['formattedText']) \
            + ';' \
            + '\n'
        return match.end()

    return pos


matchReturnChar = lambda text, pos, context: text[pos] == '\n'


def formatReturnChar(text, pos, context):
    context['formattedText'] = context['formattedText'] + text[pos]
    context['isHeadOfLine'] = True
    return pos + 1


def formatHeadOfLine(text, pos, context):
    context['formattedText'] = context['formattedText'] + \
        SyntaxEngine.generateIndent(context['indentLevel'])
    context['isHeadOfLine'] = False

    pattern = re.compile(r"[ \t]*")
    match = pattern.match(text, pos)
    return match.end()


def formatAnyChar(text, pos, context):
    context['formattedText'] = context['formattedText'] + text[pos]
    return pos + 1

if __name__ == "__main__":
    with open(r"C:\Users\Plato\Desktop\Tmp\test.shader", "r") as f:
        text = f.read()

    with open(r"C:\Users\Plato\Desktop\Tmp\test_formatted.shader", "w") as f:
        f.write(format(text))
