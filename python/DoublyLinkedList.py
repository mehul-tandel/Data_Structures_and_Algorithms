class Node():
    def __init__(self,value,next_node=None,prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_prev_node(self):
        return self.prev_node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node


class DoublyLinkedList():
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    def add_head_node(self, new_value):
        head_node = Node(new_value)
        if self.head_node == None:
            self.head_node = head_node
        else:
            head_node.set_next_node(self.head_node)
            self.head_node.set_prev_node(head_node)
            self.head_node = head_node
        if self.tail_node == None:
            self.tail_node = head_node
    def add_tail_node(self, new_value):
        tail_node = Node(new_value)
        if self.tail_node == None:
            self.tail_node = tail_node
        else:
            self.tail_node.set_next_node(tail_node)
            tail_node.set_prev_node(self.tail_node)
            self.tail_node = tail_node
        if self.head_node == None:
            self.head_node = tail_node
    def remove_head_node(self):
        removed_head = self.head_node
        if removed_head == None:
            return None
        self.head_node = removed_head.get_next_node()
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        if removed_head == self.tail_node:
            self.remove_tail_node()
        return removed_head
    def remove_tail_node(self):
        removed_tail = self.tail_node
        if removed_tail == None:
            return None
        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if removed_tail == self.head_node:
            self.remove_head_node()
        return removed_tail
    def remove_by_value(self, value_to_remove):
        current = self.head_node
        node_to_remove = None
        while current:
            if current.get_value() == value_to_remove:
                node_to_remove = current
                break
            current = current.get_next_node()
        if node_to_remove == None:
            return None
        if node_to_remove == self.head_node:
            self.remove_head_node()
        elif node_to_remove == self.tail_node:
            self.remove_tail_node()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node != None:
            string_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return string_list


#Test code
kyn_to_thn = DoublyLinkedList()
kyn_to_thn.add_head_node("Kalyan")
kyn_to_thn.add_tail_node("Dombivli")
kyn_to_thn.add_tail_node('Thane')

print(kyn_to_thn.stringify_list())

kyn_to_thn.remove_tail_node()
print(kyn_to_thn.stringify_list())

kyn_to_thn.add_head_node('Ulhasnagar')
print(kyn_to_thn.stringify_list())

kyn_to_thn.remove_head_node()
print(kyn_to_thn.stringify_list())

kyn_to_thn.add_tail_node('Diva')
kyn_to_thn.add_tail_node('Koper')
kyn_to_thn.add_tail_node('Mumbra')
kyn_to_thn.add_tail_node('Kalva')
print(kyn_to_thn.stringify_list())

kyn_to_thn.remove_by_value('Koper')
print(kyn_to_thn.stringify_list())
