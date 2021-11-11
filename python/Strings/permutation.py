# Function to return list of string permutations

def permutations(up,p):
    if up == "" :
        return p

    ch = up[0]
    ans = []
    for i in range(len(p)+1):
        left = p[:i]
        right = p[i:]
        new_p = left + ch + right
        val = permutations(up[1:],new_p)
        ans.append(val)
    return ans

#test code
s = 'abc'
print(permutations(s,""))
