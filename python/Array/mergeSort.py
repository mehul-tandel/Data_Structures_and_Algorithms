# Merge Sort algorithm

def mergeSort(arr):

    if len(arr) <= 1:
        return
    
    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l)
    mergeSort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]  # This 'arr' is the current(smaller) sub-array passed as argument(in recursion) and not the original array.
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1
    
    return arr

#test code
A = [2,5,4,7,8,3,9,0,1]
print(mergeSort(A))