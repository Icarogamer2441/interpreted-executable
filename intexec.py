import sys

stack = []
variables = {}
mode = [0]
varmode = [0]
varname = [""]

def interpret(code):
    tokens = code.split() or code.split("\t")
    string = []

    for token in tokens:
        if mode[0] == 0:
            if token == "@m1":
                mode[0] = 1
            elif token == "@m2":
                mode[0] = 2
            elif token == "@m3":
                mode[0] = 3
            elif token == "@m4":
                mode[0] = 4
                varmode[0] = 0
            elif token == "@nl":
                print("\n", end="")
            elif token == "@spc":
                print(" ", end="")
            elif token == "@m5":
                mode[0] = 5
            elif token == "@prt":
                print(stack[-1], end="")
                stack.pop()
            elif token == "@m6":
                mode[0] = 6
            elif token == "@stk":
                print(stack, end="")
            elif token == "@m7":
                mode[0] = 7
            elif token == "@m8":
                mode[0] = 8
            elif token == "@m9":
                mode[0] = 9
            elif token == "@m10":
                mode[0] = 10
            elif token == "@clr":
                stack.clear()
        elif mode[0] == 1:
            if token == "@m0":
                string = " ".join(string)
                print(string, end="")
                string = []
                mode[0] = 0
            else:
                string.append(token)
        elif mode[0] == 2:
            if token == "@m0":
                mode[0] = 0
            else:
                stack.append(int(token))
        elif mode[0] == 3:
            if token == "@m0":
                string = " ".join(string)
                stack.append(string)
                string = []
                mode[0] = 0
            else:
                string.append(token)
        elif mode[0] == 4:
            if token == "@int":
                varmode[0] = 1
            elif token == "@flt":
                varmode[0] = 2
            elif token == "@str":
                varmode[0] = 3
            elif token == "@m0":
                if varmode[0] == 3:
                    string = " ".join(string)
                    variables[varname[0]] = string
                    string = []
                mode[0] = 0
            else:
                if varmode[0] == 0:
                    varname[0] = token
                elif varmode[0] == 1:
                    variables[varname[0]] = int(token)
                elif varmode[0] == 2:
                    variables[varname[0]] = float(token)
                elif varmode[0] == 3:
                    string.append(token)
        elif mode[0] == 5:
            if token == "@m0":
                mode[0] = 0
            else:
                stack.append(float(token))
        elif mode[0] == 6:
            if token == "@m0":
                mode[0] = 0
            else:
                print(variables.get(token), end="")
        elif mode[0] == 7:
            if token == "@m0":
                variables[varname[0]] = input()
                mode[0] = 0
            else:
                varname[0] = token
        elif mode[0] == 8:
            if token == "@m0":
                variables[varname[0]] = int(variables.get(varname[0]))
                mode[0] = 0
            else:
                varname[0] = token
        elif mode[0] == 9:
            if token == "@m0":
                variables[varname[0]] = float(variables.get(varname[0]))
                mode[0] = 0
            else:
                varname[0] = token
        elif mode[0] == 10:
            if token == "@m0":
                mode[0] = 0
            else:
                stack.append(variables.get(token))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Interpreted executables (intexec)")
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        if sys.argv[1].endswith(".iexe"):
            with open(sys.argv[1], "r") as f:
                interpret(f.read())
        else:
            print("Error: use .iexe file extension")
