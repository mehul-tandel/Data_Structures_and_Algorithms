class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Inorder Traversal using stack
def inOrder(root) :
    stack = []
    ans = []
    stack.append(root)
    while root != None and len(stack)!=0:
        while root != None :
            stack.append(root)
            root = root.left
        while root == None:
            temp = stack.pop()
            ans.append(temp.data)
            root = temp.right

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
printTree(a)
print("*****")
print(inOrder(a))