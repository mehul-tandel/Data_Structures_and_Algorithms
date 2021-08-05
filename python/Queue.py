from LinkedList import Node

class Queue():
    def __init__(self, max_value):
        self.head = None
        self.tail = None
        self.max_value = max_value
        self.size = 0
    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def is_full(self):
        if self.max_value == None:
            return False
        else:
            if self.size == self.max_value:
                return True
            else:
                return False
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        else:
            return self.get_head()
        
    def dequeue(self):
        if self.is_empty():
            return "Underflow! Nothing to remove."
        else:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                head_to_remove = self.head
                self.head = head_to_remove.get_next_node()
            self.size -= 1

    def enqueue(self, value_to_append):
        new_tail = Node(value_to_append)
        if self.is_full():
            return "Overflow! No space to add."
        if self.is_empty():
            self.head = new_tail
            self.tail = new_tail
            self.size += 1
        else:
            self.tail.set_next_node(new_tail)
            self.tail = new_tail
            self.size += 1
            