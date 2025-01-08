import heapq

def solution(N, M, jobs):
    counter = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for job1, job2 in jobs:
        counter[job2] += 1
        graph[job1].append(job2)

    answer = []
    pq = []
    for job, count in enumerate(counter[1:], start = 1):
        if not count:
            heapq.heappush(pq, job)

    while pq:
        job = heapq.heappop(pq)
        answer.append(job)
        for next_job in graph[job]:
            counter[next_job] -= 1
            if not counter[next_job]:
                heapq.heappush(pq, next_job)

    print(*answer, sep = ' ')


N, M = map(int, input().split())
jobs = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, jobs)
