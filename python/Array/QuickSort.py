def partition(arr,l,r):
    pi_idx = l
    pivot = arr[pi_idx]

    while l < r:
        while l<len(arr) and arr[l] <= pivot :
            l += 1

        while arr[r] > pivot:
            r -= 1

        if l < r:
            arr[l], arr[r] = arr[r] , arr[l]
    
    arr[pi_idx],arr[r] = arr[r] , arr[pi_idx]

    return r



def quickSort(arr,l,r):

    if l < r:
        p = partition(arr,l,r)

        quickSort(arr,l,p-1)
        quickSort(arr,p+1,r)


#test code
array = [ 10, 7, 8, 9, 1, 5 ]
quickSort(array,0,len(array)-1)
print(array)
