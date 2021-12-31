def maxRectArea(arr):
    prevSmall = [] # Stack to find previous smaller element
    nextSmall = [] # Stack to find next smaller element
    pS = [0]*len(arr) # index of previous smaller element
    nS = [0]*len(arr) # index of next smaller element

    for i in range(len(arr)):
        while len(prevSmall)!=0 and prevSmall[-1][0] >= arr[i]:
            prevSmall.pop()
        if len(prevSmall) == 0 :
            pS[i] = 0
        else :
            pS[i] = prevSmall[-1][1]
        prevSmall.append([arr[i],i])

    for i in range(len(arr)-1,-1,-1):
        while len(nextSmall) != 0 and nextSmall[-1][0] >= arr[i]:
            nextSmall.pop()
        if len(nextSmall) == 0 :
            nS[i] = len(arr)
        else:
            nS[i] = nextSmall[-1][1]
        nextSmall.append([arr[i],i])

    maxArea = 0
    for i in range(len(arr)):
        maxArea = max(maxArea, arr[i]*(nS[i]-pS[i]-1))
    
    return maxArea

def largestSubmatrix(mat):
    base = [0]*len(mat[0])
    maxArea = 0
    for arr in mat:
        for i in range(len(arr)):
            if arr[i] == 0 :
                base [i] = 0
            else:
                base[i] += 1
        maxArea = max(maxArea, maxRectArea(base))
    return maxArea
    
        


# test code
# a = [4,2,1,5,6,3,2,4,2]
# print(maxRectArea(a))

mat = [[1,1,0,1,1],
        [1,1,1,1,1],
        [0,1,1,1,1],
        [1,1,1,1,1],
        [1,0,1,1,1],
        [1,1,1,1,1]]

print(largestSubmatrix(mat))