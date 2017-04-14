from enum import Enum

SymbolType = Enum('SymbolType', (
    'Prog',
    'ShaderBody',
))


class Prog:

    def __init__(self, pos, name, shader_body):
        self.kind = SymbolType.Prog
        self.pos = pos
        self.name = name  # String
        self.shader_body = shader_body  # nonterminal

    def toDict(self):
        d = {}
        d['kind'] = self.kind.name
        d['pos'] = self.pos
        d['name'] = self.name
        d['shader_body'] = self.shader_body.toDict()
        return d


class ShaderBody:

    def __init__(self, pos, raw):
        self.kind = SymbolType.ShaderBody
        self.pos = pos
        self.raw = raw

    def toDict(self):
        d = {}
        d['kind'] = self.kind.name
        d['pos'] = self.pos
        d['raw'] = self.raw
        return d


if __name__ == '__main__':
    import json

    shaderBody = ShaderBody(10, 'This is Shader Body')
    prog = Prog(1, 'Shader', shaderBody)
    # print(prog.toDict())

    t = json.dumps(prog, default=lambda obj: obj.toDict(), indent=4, sort_keys=True)
    print(t)

    # text = json.dumps(prog, default=lambda obj: obj.__dict__)
    # print(text)
