# Problem Statement: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Brute force approach with O(n^2) time complexity
# In this function we iterate through every element to check how much water can be trapped in it by comparing maximum left and right heights.

def trapRainwater(arr):

    n = len(arr)

    accumulator = 0 # to store water

    for i in range(1,n-1):

        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1,n):
            right = max(right, arr[j])

        accumulator += min(left, right)

    return accumulator

# Opitmizing the above solution, we can store left and right maximum heights in seperate arrays before running the main loop. O(n) - Time complexity. O(n) - Space complexity.

def trapRainwater2(arr):

    n = len(arr)
    accumulator  = 0

    left = [0]*n
    right = [0]*n
    
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1],arr[i])

    right[n-1] = arr[n-1]
    for i in reversed(range(n-1)):
        right[i] = max(right[i+1],arr[i])

    for i in range(n):
        accumulator += (min(left[i],right[i]) - arr[i])

    return accumulator

# Another efficient approach is to subtract height with larger previous elevation assuming there is a higher elevation coming towards right.

def trapRainwater3(arr):

    n = len(arr)
    temp = 0 # to store water from prev to upcoming prev so that if there is no upcomig pre(no higher elevation to right), temp can be subtracted from water.
    water = 0

    prev = arr[0]
    prev_idx = 0

    for i in range(1,n):
        if arr[i] >= prev :
            prev = arr[i]
            prev_idx = i
            temp = 0
        else:
            water += prev - arr[i]
            temp += prev - arr[i]

    if prev_idx < n-1 :
        water -= temp
        prev = arr[n-1]
        
        # iterate back from end to highest(prev)
        for i in range(n-1,prev_idx-1,-1):
            if arr[i] >= prev:
                prev = arr[i]
            else:
                water += prev - arr[i]

    return water