def bowl(v):
    memo = {}
    def B(i):
        if i>=len(v):
            return 0
        if i not in memo:
            memo[i] = max(B(i+1),
                v[i] + B[i+1],
                v[i]*v[i+1] + B(i+2))
        return memo[i]
    return memo[0]

def bowling(v):
    B = {}
    B[len(v)] = 0
    B[len(v)+1] = 0
    for i in reversed(range(len(v))):
        B[i] = max(B[i+1],
            v[i] + B[i+1],
            v[i]*v[i+1] + B[i+2])
    return B[0]        