'''
Problem Statement: There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)). 
'''

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return ((arr[n//2])+(arr[(n//2)-1]))//2
    else:
        return arr[n//2]

def getMedian(arr1,arr2):

    n = len(arr1)

    if n == 0:
        return -1

    elif n == 1:
        return (arr1[0]+arr2[0])/2

    elif n == 2:
        return ((max(arr1[0],arr2[0]))+(min(arr1[1],arr2[1])))/2

    else:
        m1 = median(arr1)
        m2 = median(arr2)

    # The median lies between the subarrays of start to  greater median and lesser median to end.
        if m1 > m2 :

            if n % 2 == 0:
                return getMedian(arr1[:(n//2)+1],arr2[(n//2)-1 :])
            else:
                return getMedian(arr1[:(n//2) + 1],arr2[n//2 :])
        
        else:

            if n % 2 == 0:
                return getMedian(arr1[(n//2)-1 :],arr2[:(n//2)+1])
            else:
                return getMedian(arr1[n//2 :],arr2[:(n//2)+1])


# test code
a = [1,2,3,6]
b = [4,6,8,10]

print(getMedian(a,b))