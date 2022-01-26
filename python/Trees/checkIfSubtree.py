class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(node,ans):
    if node==None:
        return ans
    inOrder(node.left,ans)
    ans.append(node.data)
    inOrder(node.right,ans)
    return ans
            
def postOrder(node,ans):
    if node==None:
        return ans
    postOrder(node.left,ans)
    postOrder(node.right,ans)
    ans.append(node.data)
    return ans

def check(tree,subtree):
    if len(subtree) > len(tree):
        return False
    for i in range(len(tree)-len(subtree)+1):
        j = 0
        if tree[i] == subtree[j]:
            while j<len(subtree):
                if tree[i+j] != subtree[j]:
                    break
                j+=1

            if j == len(subtree):
                return True
    return False
            

def checkSubtree(T,S):
    if not S:
        return True
    if not T:
        return False

    inT = inOrder(T,[])            
    inS = inOrder(S,[])
    poT = postOrder(T,[])
    poS = postOrder(S,[])

    return check(inT,inS) and check(poT,poS)


        

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
c.left = d
e.left = f

print(checkSubtree(a,e))