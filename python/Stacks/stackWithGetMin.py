# Designing a Stack data structure with a getMin() function to get minimum value item at O(1) time

class Stack:

    def __init__(self):
        self.items = []
        self.aux = []
    
    def isEmpty(self):
        return len(self.items) == 0 

    def push(self,item):
        self.items.append(item)
        if self.isEmpty():
            self.aux.append(item)
        else:
            if item < self.aux[-1] :
                self.aux.append(item)
            else:
                self.aux.append(self.aux[-1])

    def pop(self):
        if self.isEmpty():
            return
        self.aux.pop()
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def getMin(self):
        if self.isEmpty():
            return
        return self.aux[-1]

    def size(self):
        return len(self.items)
