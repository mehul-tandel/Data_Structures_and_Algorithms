def binarySearch(arr,start,end,target):
    if end < start:
        return -1
    
    mid = int((start+end)/2)
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binarySearch(arr,start,mid-1,target)
    return binarySearch(arr,mid+1,end,target)


def findPivot(arr,start,end):
    if end<start:
        return -1
    if start == end :
        return end

    mid = int((start+end)/2)
    if arr[mid] > arr[mid+1] and mid < end:
        return mid
    if arr[mid] < arr[mid-1] and mid > start:
        return mid-1
    #if arr[mid] is smaller than start, then that means the pivot is somewhere before it.
    if arr[start] >= arr[mid]:
        return findPivot(arr,start,mid-1)
    return findPivot(arr,mid+1,end)
        

def rotatedArraySearch(arr,target):
    pivot = findPivot(arr,0,len(arr)-1)
    #check if array is rotated or not
    if pivot == -1:
        return binarySearch(arr,0,len(arr)-1,target)
    if target == arr[pivot]:
        return pivot
    if target < arr[0]:
        return binarySearch(arr,pivot+1,len(arr)-1,target)
    return binarySearch(arr,0,pivot,target)

#test code
a = [4,5,6,7,1,2,3]
b = 7
print(rotatedArraySearch(a,b))
