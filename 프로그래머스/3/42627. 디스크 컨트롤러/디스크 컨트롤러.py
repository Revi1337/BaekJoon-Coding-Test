import heapq as hq

def solution(jobs):
    jobs.sort()
    current_time, sum_time, n = 0, 0, len(jobs)
    heap = []
    i = 0
    
    while i < n or heap:
        while i<n and jobs[i][0] <= current_time:
            hq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        if heap:
            duration, start = hq.heappop(heap)
            sum_time += duration + current_time - start
            current_time += duration
        else:
            current_time = jobs[i][0]
        
    return sum_time // n