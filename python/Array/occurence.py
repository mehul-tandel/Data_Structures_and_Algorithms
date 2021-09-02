# Function that counts occurences of x in a sorted array in O(logN) time complexity.

# function to find first occurence
def first(arr,l,r,x):

    if r >= l:
    
        mid = l + (r-l)//2

        if arr[mid] == x and (mid == 0 or arr[mid-1] < x):
            return mid
        elif arr[mid] < x:
            return first(arr,mid+1,r,x)
        else:
            return first(arr,l,mid-1,x)

    return -1

# function to find last occurence
def last(arr,l,r,x):

    if r >= l :
    
        mid = l + (r-l)//2

        if arr[mid] == x and (mid == len(arr)-1 or arr[mid + 1] > x):
            return mid
        elif arr[mid] > x :
            return last(arr,l,mid+1,x)
        else:
            return last(arr,mid-1,r,x)

    return -1


# main function 
def count_occurences(arr,x):

    n = len(arr)
    fo = first(arr,0,n-1,x)

    if fo == -1:
        return fo
    lo = last(arr,0,n-1,x)

    return lo-fo+1


#test code
a = [2,3,4,7,7,7,8,9]
print(count_occurences(a,7)) #prints 3