'''
Problem Statement: Given N jobs where every job is represented by following three elements of it.
Start Time
Finish Time
Profit or Value Associated
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.
'''

class Job():
    def __init__(self,start,finish,profit):
        self.start = start
        self.finish = finish
        self.profit = profit

# utility function to find last possible job (previous job) that does not conflict time range of current job.
def find_last_job(jobs,curr_job):
    lo = 0
    hi = curr_job-1

    while lo <= hi :
        mid = (lo+hi)//2
        if jobs[mid].finish <= jobs[curr_job].start:
            if jobs[mid+1].finish <= jobs[curr_job].start:
                lo = mid+1
            else:
                return mid
        else:
            hi = mid-1

    return -1


# main function to find maximum profit by scheduling(selecting) optimal set of jobs from all jobs.
def schedule(jobs):
    
    n = len(jobs)
    jobs = sorted(jobs,key = lambda j : j.finish)

    table = [0 for i in range(n)]
    table[0] = jobs[0].profit

    for i in range(1,n):
        includeProfit = jobs[i].profit
        last_job = find_last_job(jobs,i)
        if last_job != -1 :
            includeProfit += table[last_job]
        
        table[i] = max(includeProfit,table[i-1])

    return table[n-1]


# test code
job = [Job(1, 2, 50), Job(3, 5, 20), 
      Job(6, 19, 100), Job(2, 100, 200)]

print(schedule(job))