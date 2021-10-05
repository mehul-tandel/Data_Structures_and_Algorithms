'''
Problem Statement: Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of cows that are aggressive. To prevent the cows from hurting each other, you need to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.
'''

def check(x,k,stalls):

    cowsPlaced = 1
    lastPos = stalls[0]
    
    for i in range(1,len(stalls)):
        if (stalls[i] - lastPos) >= x :
            cowsPlaced += 1
            lastPos = stalls[i]

            if cowsPlaced == k :
                return True

    return False

def agressiveCows(stalls,k):

    stalls.sort()

    low = 0
    high = 10**9
    pos = 0

    while low <= high:
        mid = low + ((high-low)//2)

        if check(mid,k,stalls):
            low = mid+1
            pos = mid
        else:
            high = mid-1
    
    return pos
        