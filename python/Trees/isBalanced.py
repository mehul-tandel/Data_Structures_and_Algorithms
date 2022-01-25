def isBalanced(root):
    return helper(root)[1]

def helper(node):
    if not node:
        return (0,True) #(height,isBalanced) 
    l_height, l_balanced = helper(node.left)
    r_height, r_balanced = helper(node.right)

    return (max(l_height,r_height)+1, l_balanced and r_balanced and abs(l_height-r_height)<=1)