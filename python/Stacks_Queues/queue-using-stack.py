class MyQueue :
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,val):
        self.stack1.append(val)

    def dequeue(self):
        while len(self.stack1) != 0 :
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while len(self.stack2) != 0 :
            self.stack1.append(self.stack2.pop())
        return val

    def printQueue(self):
        print(self.stack1)
        

# test code
line = MyQueue()
line.enqueue(1)
line.enqueue(2)
line.enqueue(3)
line.enqueue(4)
line.dequeue()
line.dequeue()
line.enqueue(5)
line.printQueue()