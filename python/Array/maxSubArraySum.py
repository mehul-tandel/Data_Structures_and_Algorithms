# Kadane's algorithm

def maxSubarraySum(arr, n) :

    maxSum = 0
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        maxSum = max(currSum, maxSum)
        
        if currSum < 0:
            currSum = 0
    
    return maxSum