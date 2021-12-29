# Using list as stack

def reverse(strn):
    stack = []
    for s in strn:
        stack.append(s)
    strn = ""
    for i in range(len(stack)):
        strn += stack.pop()
    return strn

#test code
a = "abcdef"
print(reverse(a))