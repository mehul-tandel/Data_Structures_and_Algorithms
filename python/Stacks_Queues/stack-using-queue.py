class MyStack:
    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self,val):
        while len(self.que1) != 0 :
            self.que2.append(self.que1.pop(0))
        self.que1.append(val)
        while len(self.que2) != 0 :
            self.que1.append(self.que2.pop(0))

    def pop(self):
        if len(self.que1) == 0 :
            return
        return self.que1.pop(0)
    
    def printStack(self):
        print(self.que1)

# test code
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.printStack()