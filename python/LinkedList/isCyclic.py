from LinkedList import *

def isCyclic(ll):
    fast = ll.get_head_node()
    slow = ll.get_head_node()
    
    while (fast != None and fast.get_next_node() != None) and slow != None :
        fast  = fast.get_next_node().get_next_node()
        slow  = slow.get_next_node()
        if (slow==fast) :
            return True
    
    return False

def cycleLength(ll):
    fast = ll.get_head_node()
    slow = ll.get_head_node()
    
    while (fast != None and fast.get_next_node() != None) and slow != None :
        fast  = fast.get_next_node().get_next_node()
        slow  = slow.get_next_node()
        if (slow==fast) :
            temp = slow.get_next_node()
            count = 2
            while temp != fast :
                temp = temp.get_next_node()
                if temp != fast : #what if there are only 2 nodes in the cycle.
                    count += 1
            
            return count
    
    return 0