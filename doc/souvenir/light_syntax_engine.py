import re

class SyntaxEngine(object):
    '''
    matcher, (text, pos, context) -> True/False
    driver, (text, pos, context) -> void
    '''

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.matchers = {}
        self.drivers = {}
        self.context = {}
        pass

    def add(self, key, matcher, driver):
        self.matchers[key] = matcher
        self.drivers[key] = driver

    def match(self, key):
        if self.matchers[key](self.text, self.pos, self.context):
            self.pos = self.drivers[key](self.text, self.pos, self.context)
            return True

        return False


    # match的扩展版，用来搜寻必须的匹配。会跳过所有seperator
    def require(self, key = None, *, matcher = None, driver = None):
        pattern = re.compile(r'\s*')
        print("====================")
        print(self.pos)
        # print(self.text)
        newPos = pattern.match(self.text, self.pos).end()

        # branch-1
        if key and self.matchers[key](self.text, newPos, self.context):
            self.pos = self.drivers[key](self.text, newPos, self.context)
            return True

        # branch-2
        if matcher and driver and matcher(self.text, newPos, self.context):
            self.pos = driver(self.text, newPos, self.context)
            return True

        # todo, exist engine immediately
        print('Require Error!')
        return False


    def isEnd(self):
        # print(self.pos)
        return self.pos >= len(self.text)

    ## Toolkits ##
    @staticmethod
    def generateRegexMatcher(regexString):
        def regexMatcher(text, pos, context): 
            pattern = re.compile(regexString)
            return pattern.match(text, pos)

        return regexMatcher


class BasicFormater(object):

    ## Toolkits ##
    @staticmethod
    def generateIndent(level):
        return " "*4*level


    @staticmethod
    def skipSpaces(text, pos):
        pattern = re.compile(r"[ \t]*")
        return pattern.match(text, pos).end()


    @staticmethod
    def trimSpaceFromTail(text):
        newTail = len(text)
        while newTail > 0 and text[newTail-1] == ' ':
            newTail = newTail -1
        return text[0:newTail]

    @staticmethod
    def trimSpaceReturnFromTail(text):
        newTail = len(text)
        while newTail > 0 and ( text[newTail-1] == ' ' or text[newTail-1] == '\n'):
            newTail = newTail -1
        return text[0:newTail]

    @staticmethod
    def formatEmptyString(text, pos, context):
        return pos
