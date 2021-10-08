'''
Problem Statement : IEEE is having its AGM next week and the president wants to serve cheese prata after the meeting. The subcommittee members are asked to go to food connection and get P(P<=1000) pratas packed for the function. The stall has L cooks(L<=50) and each cook has a rank R(1<=R<=8). A cook with a rank R can cook 1 prata in the first R minutes 1 more prata in the next 2R minutes, 1 more prata in 3R minutes and so on(he can only cook a complete prata) ( For example if a cook is ranked 2.. he will cook one prata in 2 minutes one more prata in the next 4 mins an one more in the next 6 minutes hence in total 12 minutes he cooks 3 pratas in 13 minutes also he can cook only 3 pratas as he does not have enough time for the 4th prata). The webmaster wants to know the minimum time to get the order done. Please write a program to help him out.
'''

def minTime(arr,k):

    arr.sort()
    r = arr[0]
    total_time = 0
    i = 1
    while i <= k:
        total_time += (r*i)
        i += 1

    l = 0
    r = total_time
    min_time = total_time

    while l <= r:
        mid = l + (r-l)//2

        if isPossible(mid,k,arr):
            min_time = mid
            r = mid - 1
        else:
            l = mid + 1

    return min_time

def isPossible(x,k,arr):

    paratas = 0

    for rank in arr :
        time = x
        i = 1
        while time > 0:
            time -= (rank*i)
            if time >= 0 :
                paratas += 1
            i += 1
        if paratas >= k:
            return True
    
    return False

# test code
k = 10
ranks = [1,2,3,4]
print(minTime(ranks,k))
