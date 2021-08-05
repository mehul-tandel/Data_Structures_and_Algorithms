#Node stores a data value in "value" and stores a variable containing next node in "next_node"
class Node():
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node
        

#LinkedList contains Nodes which can be traversed using next_node reference
class LinkedList():
    def __init__(self, value=None):
        self.head_node = Node(value)
    def get_head_node(self):
        return self.head_node
    def insert_new_head_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    def insert_new_node(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node
        if self.head_node:
            while current_node.get_next_node():
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)
        else:
            self.head_node = new_node
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node != None:
            string_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return string_list
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()

#function to get nth last node from given Linked list
def get_nth_node(linked_list, n):
    count = 1
    nth_node = None
    current = linked_list.get_head_node()
    while current:
        current = current.get_next_node()
        if count == n:
            nth_node = linked_list.get_head_node()
        if count > n:
            nth_node = nth_node.get_next_node()
        count += 1
    return nth_node

#function to get middle node from given linked list
def get_middle_node(linked_list):
    fast = linked_list.get_head_node()
    slow = linked_list.get_head_node()
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow

#Test code
#Creating Linked list and adding nodes
my_ll = LinkedList(5)
my_ll.insert_new_head_node(10)
my_ll.insert_new_node(4)
my_ll.insert_new_node(3)
my_ll.insert_new_node(555)
my_ll.insert_new_node(359)
my_ll.insert_new_head_node(15)
my_ll.insert_new_head_node(16)
print(my_ll.stringify_list())

#Getting nth last node
print(get_nth_node(my_ll, 3).get_value())

#Getting middle node
print(get_middle_node(my_ll).get_value())