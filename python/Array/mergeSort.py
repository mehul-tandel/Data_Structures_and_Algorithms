def merge(arr,L,R):
    i,j,k = 0,0,0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr)>1 :
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(arr,L,R)


def mergeSort2(arr):
    l = 0
    r = len(arr)-1
    if l<r:
        mid = (l+r)//2
        L = arr[:mid+1]
        R = arr[mid+1:]
        mergeSort2(L)
        mergeSort2(R)
        merge(arr,L,R)


# test code
a = [4,6,2,3,9,7,8,1,5]
mergeSort2(a)
# mergeSort(a)
print(a)