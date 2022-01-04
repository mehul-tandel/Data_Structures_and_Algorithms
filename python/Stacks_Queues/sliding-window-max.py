# Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

from collections import deque

def slidingWindowMax(arr,k):
    if not arr or k == 0:
        return arr

    ans = []
    queue = deque()
    
    # Created first window
    for i in range(k):
        while len(queue) != 0 and queue[-1] <= arr[i] :
            queue.pop()
        queue.append(i) # Queue stores index of that number istead of number itself so that we'll know when it will go out of the window
    ans.append(arr[queue[0]])

    for i in range(k,len(arr)):
        while queue and arr[queue[-1]] <= arr[i] :
            queue.pop()
        queue.append(i)
        ans.append(arr[queue[0]])

        if queue and queue[0] <= i-k :
            queue.popleft()        
     
    return ans


#test code
a = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 7
print(slidingWindowMax(a,k))