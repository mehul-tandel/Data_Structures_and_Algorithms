# Using list as stack

def insertAtBottom(stack,item):
    if len(stack) == 0 :
        stack.append(item)
    else :
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)

def reverseStack(stack):
    if len(stack) == 0 :
        return stack
    item = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack,item)

#test code
stack = [1,2,3,4]
reverseStack(stack)
print(stack)