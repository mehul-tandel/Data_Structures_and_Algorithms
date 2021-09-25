'''
Problem Statement: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
'''

def nextPermutation(nums):
    n = len(nums)
    swapped = False # to check if any swap occur
    
    for i in range(n-1,0,-1):
        
        if nums[i] > nums[i-1]:
            
            if i == n-1: # edge case as the for loop below skips it
                nums[i-1],nums[i] = nums[i],nums[i-1]
            
            # Checks for last number greater than nums[i-1] and swaps them
            for j in range(n-1,i-1,-1): 
                if nums[j] > nums[i-1]:
                    nums[i-1],nums[j] = nums[j],nums[i-1]
                    break
            
            # Reverse the numbers from i to n-1
            k = 1
            for j in range(i,i + ((n-i)//2)):
                nums[j],nums[n-k] = nums[n-k],nums[j]
                k += 1
            
            swapped = True
            break
   
    # if no swap occured, then numbers are in decreasing order    
    if swapped == False:
        nums.reverse()

# It appears as if the time complexity is O(n^2) but each loop runs only once even in the worst case. So this algorithm run in linear time O(n).