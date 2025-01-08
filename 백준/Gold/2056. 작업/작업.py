from collections import deque

def solution(N, jobs):
    counter, times = [[0] * (N + 1) for _ in range(2)]
    graph = [[] for _ in range(N + 1)]

    for job, entry in enumerate(jobs, start = 1):
        time, _, *next_jobs = entry
        times[job] = time
        for nj in next_jobs:
            graph[nj].append(job)
            counter[job] += 1

    dp = [0] * (N + 1)
    queue = deque()
    for job in range(1, N + 1):
        if not counter[job]:
            queue.append(job)
            dp[job] = times[job]

    while queue:
        job = queue.popleft()
        for nj in graph[job]:
            counter[nj] -= 1
            dp[nj] = max(dp[job] + times[nj], dp[nj])
            if not counter[nj]:
                queue.append(nj)

    print(max(dp))

N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]
solution(N, jobs)
