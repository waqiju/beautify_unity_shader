import os


def import_from_file(relativePath):
    currentModulePath = os.path.abspath(os.path.dirname(__file__))
    targetModulePath = os.path.abspath(os.path.join(currentModulePath, relativePath))
    targetModuleFolder, targetModule = os.path.split(targetModulePath)

    import sys, importlib
    sys.path.append(targetModuleFolder)
    return importlib.import_module(targetModule)


lexer = import_from_file('../app/lexer')


shaderFolder = r'E:\1_Downloads\2_Protable_Program\Sublime Text Build 3126 x64\Data\Packages\UnityShader\builtin_shaders-5.5.0f3'
for path, dirs, files in os.walk(shaderFolder):
    for file in files:
        if file[-7:] != '.shader':
            continue

        print(file)
        with open(os.path.join(path, file)) as f:
            buf = f.read()
            lexer.lexicalAnalyze(buf)
        print('')
