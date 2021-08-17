'''
Problem Statement
Given an array “A” of N integers and you have also defined the new array “B” as a concatenation of array “A” for an infinite number of times.
For example, if the given array “A” is [1,2,3] then, infinite array “B” is [1,2,3,1,2,3,1,2,3,.......].
Now you are given Q queries, each query consists of two integers “L“ and “R”. Your task is to find the sum of the subarray from index “L” to “R” (both inclusive) in the infinite array “B” for each query.
'''

def sumInRanges(arr, n, queries, q):

    sums = []
    m = 1000000007
    
    for query in queries:
        sum = 0
        count = 0 
        flag = True
        while flag:
            for j in arr:
                count += 1
                if count > query[1]:
                    flag = False
                    break
                if count >= query[0]:
                    sum += j
                    sum = sum%m
        sums.append(sum)
    return sums



#Approach2
#this function returns the sum of all the elements of the infinite-array from start to index x
def sumArray(arr, x, n):
        
    m = 10**9 + 7
    sum = 0
    for i in range(x):
        sum += arr[i%n]
        sum %= m
        
    return sum
            
            
            
def sumInRanges2(arr, n, queries, q):
    
    sums = []
    m = 10**9 + 7
    for query in queries:
        l = query[0]
        r = query[1]
        
        lsum = sumArray(arr,l-1,n)%m
        rsum = sumArray(arr,r,n)%m
        
        sums.append(rsum-lsum)
        
    return sums


#Test code
N = 2
A = [11,11]
lr = [[1,2],[1,3],[2,3],[2,4],[1,10]]
Q = 5
print(sumInRanges(A, N, lr, Q))

