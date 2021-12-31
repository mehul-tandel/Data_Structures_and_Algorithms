def infixToPostfix(strn):
    stack = []
    ans = ""
    for s in strn :
        if s.isalpha() :
            ans += s
        elif s == '(' :
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(' :
                ans += stack.pop()
            stack.pop()
        else :
            while len(stack) != 0 and precedense(s) <= precedense(stack[-1]) :
                ans += stack.pop()
            stack.append(s)
    while len(stack) != 0 :
        ans += stack.pop()
    return ans

def precedense(ch) :
    if ch == '+' or ch == '-' :
        return 1
    elif ch == '*' or ch == '/' :
        return 2
    elif ch == '^' :
        return 3
    else :
        return -1

# test code
exp = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPostfix(exp))