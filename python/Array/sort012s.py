def sort012(arr,n):
    zeros = 0
    ones = 0
    twos = 0
    ans=[]
    for i in arr:
        if i == 0:
             zeros += 1
        if i == 1:
            ones += 1
        if i == 2:
            twos += 1
    ans = [0]*zeros + [1]*ones + [2]*twos
    return ans

arr = [2,1,0,2,1,0,2,1,0,2,0,1,2,0,2]
n = 15
print(sort012(arr,n))