# function to apply binary search on a row
def binarySearch(matrix,row,x):
    m = len(matrix[row])
    l = 0
    r = m-1
    mid = 0
    while l <= r :
        mid = l + (r-l)//2
        if matrix[row][mid] == x :
            return mid
        elif matrix[row][mid] < x :
            l = mid + 1
        else:
            r = mid - 1
    return -1

# function to find the row on which binary search has to be applied
def findRow(matrix,x):
    n = len(matrix)
    m = len(matrix[0])

    l = 0
    r = n-1
    mid = 0
    while l <= r :
        mid = l + (r-l)//2
        if matrix[mid][0]<x and matrix[mid][m-1]>x :
            return binarySearch(matrix,mid,x)
        if matrix[mid][0]>x :
            r = mid - 1
        if matrix[mid][m-1]<x:
            l = mid + 1
    return -1