'''
Problem Statement
Given an array ‘ARR’ and an integer ‘K’, your task is to find all the count of all sub-arrays whose sum is divisible by the given integer ‘K’.
'''

def subArrayCount(arr, k):

    count = 0
   
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum%k == 0:
                count += 1
    return count