# Median of two sorted arrays of different sizes
#O(min(logn,logm)) time complexity

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return ((arr[n//2])+(arr[(n//2)-1]))//2
    else:
        return arr[n//2]

# median of 2 is their average
def mo2(a,b):
    return (a+b)//2

# median of 3 is the middle element
def mo3(a,b,c):
    return a+b+c-max(a,max(b,c))-min(a,min(b,c))

# median of 4 is average of middle 2 elements
def mo4(a,b,c,d):
    return (a+b+c+d-(max(a,(max(b,max(c,d)))))-min(a,min(b,min(c,d))))//2

def getMedian(arr1,arr2):
# assumes n < m
    n = len(arr1)
    m = len(arr2)

    # base cases / edge cases
    if n == 0:

        if m == 0:
            return -1
        if m == 1:
            return arr2[0]
        return median(arr2)

    elif n == 1:

        if m == 1:
            return mo2(arr1[0],arr2[0])
        if m == 2:
            return mo3(arr1[0],arr2[0],arr2[1])
        
        # if m is even, total will be odd
        if m % 2 == 0 :
            return mo3(arr2[(m//2)-1],arr2[m//2],arr1[0])
        
        # if m is odd, total will be even
        return mo2(arr2[m//2],mo3(arr1[0],arr2[(m//2)-1],arr2[(m//2)+1]))

    elif n == 2 :

        if m == 2:
            return mo4(arr1[0],arr1[1],arr2[0],arr2[1])

        # if m is even, total is even
        if m % 2 == 0 :
            return mo4(arr2[m//2],arr2[(m//2)-1], max(arr1[0],arr2[(m//2)-2]), min(arr1[1],arr2[(m//2)+1]))
        
        # if m is odd, total is odd
        return mo3(arr2[m//2],max(arr1[0],arr2[(m//2)-1]), min(arr1[1],arr2(m//2)+1))

    # recurrsion case

    mid1 = arr1[n//2]
    mid2 = arr2[m//2]

    if mid1 > mid2 :
        return findMedian(arr1[:(n//2)+1],arr2[m//2 :])

    return findMedian(arr2[:(m//2)+1],arr1[n//2 :])

# function to keep smaller array first
def findMedian(arr1,arr2):
    n = len(arr1)
    m = len(arr2)

    if n > m :
        return getMedian(arr2,arr1)
    return getMedian(arr1,arr2)

# test code
a = [-5,3,6,12,15]
b = [-12,-10,-6,-3,4,10]

print(getMedian(a,b))