 #function to multiply integers given in the form of a list.

def multiply(a,b):
    
    sign = -1 if(a[0]< 0 ^ b[0]<0) else 1
    ans = [0]*(len(a)+len(b))

    a[0],b[0] = abs(a[0]), abs(b[0])

    for i in reversed(range(a)):
        for j in reversed(range(b)):
            ans[i+j+1] += a[i]*b[j]
            ans[i+j] += ans[i+j+1]//10
            ans[i+j+1] %= 10

    ans = ans[next((i for i,x in enumerate(ans) if x!=0),len(ans)):] or [0]

    return [sign*ans[0]]+ans[1:]

