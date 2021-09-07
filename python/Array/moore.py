# Find marjority element in the array (Moore's algorithm)

def majorityElement(arr):
    
    n = len(arr)
    maj_idx = 0
    count = 0

    for i in range(n):
        if arr[i] == arr[maj_idx]:
            count += 1
        else :
            count -= 1

        if count == 0:
            maj_idx = i
            count = 1

    count = 0
    for i in range(n):
        if arr[i] == arr[maj_idx]:
            count += 1

    if count >= n//2:
        return arr[maj_idx]
    
    return -1