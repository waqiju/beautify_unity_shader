

def main():
    testFile = r'D:\1_Workspace\github\beautify_unity_shader\test\test.shader'
    with open(testFile) as f:
        buf = f.read()
        print(buf)


if __name__ == '__main__':
    main()