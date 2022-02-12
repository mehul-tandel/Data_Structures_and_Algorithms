def fibo(n):
    memo = [0]*(n+1)
    memo[0] = 0
    memo[1] = 1

    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

def fiboo(n):
    memo = {}
    def fi(i):
        if i<2: return i
        if i not in memo:
            memo[i] = fi(i-1)+fi(i-2)
        return memo[i]
    return fi(n)

print(fibo(20))
print(fiboo(20))