class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0 

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)


def deleteMid(stack,size,curr):
    if stack.isEmpty() or curr >= size:
        return

    temp = stack.pop()
    deleteMid(stack,stack.size(),curr+1)
    if curr != stack.size() :
        stack.push(temp)

#test code
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)

print(a.items)
deleteMid(a,a.size(),0)
print(a.items)