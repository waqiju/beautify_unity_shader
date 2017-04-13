from lex_rules import rules
import error_message


def lexicalAnalyze(inputText):
    pos = 0
    tokens = []
    error_message.reset()

    while pos < len(inputText):
        for rule in rules:
            match = rule['pattern'].match(inputText, pos)
            if match:
                matchText = match.group()
                tokens.append(rule['action'](matchText))
                error_message.forward(matchText)
                pos = match.end()
                break

    return tokens


if __name__ == '__main__':
    import os
    testFile = os.path.abspath( os.path.join(__file__, r"../../test/test.shader") )

    with open(testFile) as f:
        buf = f.read()
        tokens = lexicalAnalyze(buf)

    outputFile = os.path.abspath( os.path.join(__file__, r"../../test/lex_output.txt") )
    with open(outputFile, 'w') as f:
        for token in tokens:
            f.write(str(token))
            f.write('\n')
