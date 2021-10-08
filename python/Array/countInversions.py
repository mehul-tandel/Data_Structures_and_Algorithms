def mergeSort(arr):
    n = len(arr)
    return _mergeSort(arr,0,n-1)

def _mergeSort(arr,l,r):
    if r<=l:
        return 0
        
    inv = 0
    mid = l + (r-l)//2

    L = arr[:mid+1]
    R = arr[mid+1 :]

    inv += _mergeSort(L,l,mid)
    inv += _mergeSort(R,mid+1,r)

    inv += merge(arr,L,R,l,mid,r)

    return inv
    

def merge(arr,L,R,l,mid,r):

    i,j,k = 0,0,0
    inv = 0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            inv += (mid-i+1)
            j += 1
        k += 1

    while i<len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j<len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
    return inv

# test code

a = [4,2,1,3]
b = mergeSort(a)
print(b)
print(a)