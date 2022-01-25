from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def zigzag(root):

    ans = []
    ltr = [] #push children left to right in rtl stack
    rtl = [] #push children right to left in ltr stack

    ltr.append(root)

    while len(ltr)!=0 or len(rtl)!=0 :
        while len(ltr)!=0 :
            temp = ltr.pop()
            ans.append(temp.data)
            if temp.left != None:
                rtl.append(temp.left)
            if temp.right != None:
                rtl.append(temp.right)

        while len(rtl)!=0 :
            temp = rtl.pop()
            ans.append(temp.data)
            if temp.right != None:
                ltr.append(temp.right)
            if temp.left != None:
                ltr.append(temp.left)

    return ans

def printTree(root):
    if root.left:
        printTree(root.left)
    print(root.data)
    if root.right:
        printTree(root.right)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)

a.left = c
a.right = b
b.left = f
c.left = d
c.right = e
d.left = i
d.right = h
e.left = g

# printTree(a)
print(zigzag(a))