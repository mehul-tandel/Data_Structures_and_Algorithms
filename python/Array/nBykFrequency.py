'''
Problem Statement: Given an array arr[] of size N and an element k. The task is to find all elements in array that appear more than n/k times.
'''

def frequency(arr,k):
    n = len(arr)

    # create a temp array to store the count of occurrences of arr[elements]
    # there can only be (k-1) elements which occur more than n/k times becasue if k elements occur n/k times then all elements of n are in those k elements and there is no room for any other element or elements to exceed n/k which means no element will be greater than n/k.
    temp = [[0 for i in range(2)] for i in range(k)]
    ans = 0
    #storing counts of candidates in temp

    for i in range(n): #O(n(k+k))

        j = 0

        # increase the counter of arr[i] in temp if it exists in temp[].
        while j < k:
            if temp[j][0] == arr[i]:
                temp[j][1] += 1
                break
            j += 1

        # if arr[i] does not exist in temp[], add arr[i] to temp.
        if j == k:
            l = 0
            while l < k :
                if temp[l][1] == 0:
                    temp[l][0] = arr[i]
                    temp[l][1] = 1
                    break
                l += 1
            
            # if temp is full and there is no space to add arr[i] then decrease all counts by 1.
            if l == k:
                for m in range(k):
                    temp[m][1] -= 1

    # all elements in temp[] are candidates that need to be checked 
    for i in range(k): #O(k(n))
        count = 0
        for j in range(n):
            if temp[i][0] == arr[j]:
                count += 1

        if count > (n/k):
            ans += 1
    
    return ans

# Time complexity is O(nk)

# test code

a = [3,1,2,2,1,2,3,3]
b = 4
print(frequency(a,b))