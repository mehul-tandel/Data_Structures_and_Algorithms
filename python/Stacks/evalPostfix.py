def evaluatePostfix(strn):
    stack = []
    for s in strn :
        if s.isnumeric() :
            stack.append(int(s))
        else :
            b = stack.pop()
            a = stack.pop()

            if s == '+' :
                stack.append(a+b)
            elif s == '-':
                stack.append(a-b)
            elif s == '*' :
                stack.append(a*b)
            elif s == '/' :
                stack.append(a/b)
            elif s == '^' :
                stack.append(a^b)
            else :
                print("Invalid operator")
                return
    return stack[0]

# test code
exp = "231*+9-"
print(evaluatePostfix(exp))