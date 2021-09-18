def heapify(arr,n,i): #O(logN) time compexity as heap is a near complete binary tree(which has logarithmic number of steps or levels)

    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[l]>arr[largest]:
        largest = l

    if r<n and arr[r]>arr[largest]:
        largest = r

    if largest != i: #change the root and heapify again
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def heapSort(arr):

    n = len(arr)

    for i in range((n//2) - 1, -1, -1): # build max heap # i goes n/2 -1 to 0 index building from bottom up.
        heapify(arr,n,i)   

    for i in range(n-1,0,-1): # extract max by swapping root with last node and removing the last node by decrementing the array
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0) # here i(size of heap to heapify) is going from n-1 to 0 and 0 is the root
        