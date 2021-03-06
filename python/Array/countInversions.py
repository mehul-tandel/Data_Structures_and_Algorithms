def merge(arr,L,R):
    i,j,k = 0,0,0
    inv = 0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            inv += len(L)-i
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
    
    return inv


def mergeSort(arr):
    inv = 0
    if len(arr)>1 :
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        inv += mergeSort(L)
        inv += mergeSort(R)
        inv += merge(arr,L,R)
    return inv

# test code

a = [4,8,5,6,7,1,3,2]
b = mergeSort(a)
print(b)
print(a)