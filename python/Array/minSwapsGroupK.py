'''
Problem Statement: Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.
'''
# Count the number of elements less than or equal to k. If we swap elements to bring them all together, they will fit in the subarray of size count.
# So a sliding window of size count is iterated and minimum number of greater elements are tracked to swap, which will in turn give the subarray of size count with all the required elements.
def minSwap (arr, n, k) : 
    
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1
            
    bad = 0
    
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    ans = bad
    j = count
    
    for i in range(n):
        if j == n :
            break
        
        if arr[i] > k :
            bad -= 1
            
        if arr[j] > k :
            bad += 1
            
        ans = min(bad,ans)    
        j += 1
        
    return ans 