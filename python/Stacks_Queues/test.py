from collections import deque

def maxSlidingWindow(nums, k: int):
    if not nums or k == 0:
        return nums
    deq, result = deque(), []
    for i in range(len(nums)):
        if i >= k:
            result.append(nums[deq[0]])   # save cur max from deque
            if deq[0] < i - k + 1:        # popleft item if left item leaves window
                deq.popleft()
        while deq and nums[i] > nums[deq[-1]]:  # pop every smaller element from end
            deq.pop()
        deq.append(i)
    
    result.append(nums[deq[0]])
    return result

#test code
a = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 7
print(maxSlidingWindow(a,k))      