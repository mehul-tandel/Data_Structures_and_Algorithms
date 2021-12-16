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
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
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
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        
# Reverse a section of linked list
def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

    if left == right:
        return head

    curr = head
    prev = None
    
    for i in range(left-1): # curr pointer to left
        prev = curr
        curr = curr.next
    last = prev #last node before left
    end = curr #left node (to be connected to node after right)
    
    for i in range(right-left+1): # reversing right to left
        next = curr.next

        curr.next = prev
        prev = curr
        curr = next
        
    if end != None:
        end.next = curr # left node pointing to node after right
    # If left is head, head will change
    if last != None:
        last.next = prev # last node before left pointing to right
    else:
        head = prev

    return head
    

# Function to find middle node
def middle(head):
    fast = slow = head

    while fast != None and fast.next != None :
        fast = fast.next.next
        slow = slow.next

    return slow

# Check if linked list is palindromic
def isPalindrome(head: Optional[ListNode]) -> bool:
    if head == None or head.next == None :
        return head
    mid  = middle(head)
    newMid = reverse(mid)
    f = head
    s = newMid
    while s != None :
        if f.val != s.val :
            break
        f = f.next
        s = s.next
    flag = False
    if f == newMid :
        flag = True
    if s == None:
        flag = True
    reverse(newMid)

    return flag


# Reorder list 
def reorderList(head: Optional[ListNode]) -> None:
    mid = middle(head)
    midNext = mid.next
    midNext = reverse(midNext)
    mid.next = None
    head2 = midNext

    while head2 != None :
        newHead = head.next
        head.next = head2
        newHead2 = head2.next
        head2.next = newHead
        head = newHead
        head2 = newHead2


# Reverse nodes in k groups
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    start = head
    end = head
    flag = True
    oldStart = None
    while flag :
        for i in range(k-1):
            end = end.next
            if end == None:
                flag = False
                break
        if flag == False :
            break
        newStart = end.next
        # reverse start to end
        curr = start
        prev = newStart
        while curr != newStart :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if oldStart != None:
            oldStart.next = prev
        else: # new head
            head = prev
        oldStart = start
        if newStart == None :
            break
        start = newStart
        end = newStart
    return head


# Rotate List
def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head == None:
        return head
    node = head
    length = 0
    while node != None :
        if node.next == None:
            last = node
        node = node.next
        length += 1
    k = k%length
    if k == 0 :
        return head
    newEnd = length - k
    newLast = head
    for i in range(newEnd-1):
        newLast = newLast.next
    last.next = head
    newHead = newLast.next
    newLast.next = None
    return newHead

# Remove cycle
def removeCycle(head):
    length = getLength(head)
    if length == 0 :
        return
    f = head
    s = head
    while length > 0 :
        f = f.next
        length -= 1
    while f.next != s.next :
        f = f.next
        s = s.next
    f.next = None
    return


# Merge Sort on LL
def mergeSort(head):
    fast = slow = head
    temp = head
    while fast != None and fast.next != None :
        fast = fast.next.next
        temp = slow
        slow = slow.next
    temp.next = None
    left = mergeSort(head)
    right = mergeSort(slow)
    return merge(left,right)

def merge(left,right):
    start = ListNode(0)
    head = start
    while left != None and right != None :
        if left.data < right.data :
            start.next = left
            left = left.next
            start = start.next
        else:
            start.next = right
            right = right.next
            start = start.next
    while left != None :
        start.next = left
        left = left.next
        start = start.next
    while right != None :
        start.next = right
        right = right.next
        start = start.next
    return head.next



# #test code
# a = ListNode(1)
# a.next = ListNode(2)
# b = a.next
# c = b.next = ListNode(3)
# d = c.next = ListNode(4)
# e = d.next = ListNode(5)
# e.next = b

# def printList(head):
#     while head != None :
#         print(head.val)
#         head = head.next
# removeCycle(a)
# printList(a)
# r = reverseKGroup(a,2)
# print("***")
# printList(r)