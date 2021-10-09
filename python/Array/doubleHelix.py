'''
Problem Statement : Two ﬁnite, strictly increasing, integer sequences are given. Any common integer between the two sequences constitute an intersection point.

You can ‘walk” over these two sequences in the following way:
1. You may start at the beginning of any of the two sequences. Now start moving forward.
2. At each intersection point, you have the choice of either continuing with the same sequence you’re currently on, or switching to the other sequence.

The objective is ﬁnding a path that produces the maximum sum of data you walked over.
'''

def maxSum(arr1,arr2):
    sum1 = 0
    sum2 = 0
    i,j = 0,0
    n1 = len(arr1)
    n2 = len(arr2)
    ans = 0

    while i<n1 and j<n2:
        if j < n2 and arr1[i] < arr2[j] :
            sum1 += arr1[i]
            i += 1
        if i < n1 and arr2[j] < arr1[i] :
            sum2 += arr2[j]
            j += 1

        if i<n1 and j<n2 and arr1[i] == arr2[j] :
            ans += max(sum1,sum2)
            ans += arr1[i]
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    while i<n1 :
        sum1 += arr1[i]
        i += 1
    while j < n2 :
        sum2 += arr2[j]
        j += 1

    ans += max(sum1,sum2)

    return ans


# test code
a = [3,5,7,9,20,25,30,40,55,56,57,60,62]
b = [1,4,7,11,14,25,44,47,55,57,100]
print(maxSum(a,b))