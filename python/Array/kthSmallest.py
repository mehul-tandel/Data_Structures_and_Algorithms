def kth(arr1,arr2,n,m,k):

    if n == 1 or m == 1 :
        if m == 1:
            arr1,arr2 = arr2 , arr1
            m,n = n,m
        if k == 1 :
            return min(arr1[0],arr2[0])
        elif k == 2 :
            return max(arr1[0],arr2[0])    #both are sorted arrays so first element from both are smallest, after merging, greater of two will be second.
        else:
            if arr2[k-1] < arr1[0]:
                return arr2[k-1]
            else:
                return max(arr1[0],arr2[k-2])

    mid1 = (n-1)//2
    mid2 = (m-1)//2

    if mid1+mid2+1 < k :
        if arr1[mid1] < arr2[mid2]:
            return kth(arr1[mid1+1:],arr2,n-mid1-1,m,k-mid1-1)
        else:
            return kth(arr1,arr2[mid2+1:],n,m-mid2-1,k-mid2-1)
    else:                                             #>=k
        if arr1[mid1] < arr2[mid2]:
            return kth(arr1,arr2[:mid2+1],n,mid2+1,k) #including mid
        else:
            return kth(arr1[:mid1+1],arr2,mid1+1,m,k)

# test code
# arr1 = [2, 3, 6, 7, 9]
# arr2 = [1, 4, 8, 10]
# k = 5
# print(kth(arr1,arr2,len(arr1),len(arr2),k))