from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Function to get cycle length
def getLength(head):
    fast = head
    slow = head

    while fast != None or fast.next != None :
        fast = fast.next.next
        slow = slow.next
        if (slow == fast) :
            temp = slow
            temp = temp.next
            count = 2
            while (temp.next != fast) :
                temp = temp.next
                count += 1
            return count
    return 0

# Function to find the first node of the cycle in a linked list
def findFirst(head):
    length = getLength(head)
    if length == 0 :
        return
    f = head
    s = head
    while length > 0 :
        f = f.next
        length -= 1
    while f != s :
        f = f.next
        s = s.next
    return f

# Funtion to remove duplicates
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return head
    node = head
    while node.next != None :
        if node.next.val == node.val :
            node.next = node.next.next
        else:
            node = node.next
    return head

# Funtion to merge 2 sorted linked lists
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    first = list1
    second = list2
    ans = ListNode(0)
    head = ans

    while first != None and second != None :
        if first.val < second.val :
            ans.next = first
            ans = ans.next
            first = first.next
        else :
            ans.next = second
            ans = ans.next
            second = second.next
    
    while first != None :
        ans.next = first
        ans = ans.next
        first = first.next
    
    while second != None :
        ans.next = second
        ans = ans.next
        second = second.next

    return head.next

# Function to reverse a linked list
# Recursive funtion
def reverseRecur(head): 
    return reverseList(head,None)

def reverseList(head,newHead): 
    if head == None :
        return newHead
    next = head.next
    head.next = newHead
    return reverseList(next,head)

# Iteratively reverse linked list
def reverse(head):
    prev = None
    curr = head

    while curr != None :
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
        