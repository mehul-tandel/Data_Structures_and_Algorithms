# Using list as stack

def sortStack(stack):
    if len(stack) == 0 :
        return stack
    temp = stack.pop()
    sortStack(stack)
    sortedInsert(stack, temp)

def sortedInsert(stack, item):
    if len(stack) == 0 or stack[-1] > item :
        stack.append(item)
        return stack
    temp = stack.pop()
    sortedInsert(stack, item)
    stack.append(temp)

#test code
a = [3,52,7,5,1,6,9]
sortStack(a)
print(a)