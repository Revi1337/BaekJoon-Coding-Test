import sys
from collections import deque

input = sys.stdin.readline

def solution(n, m, pds):
    queue = deque()
    priority = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for cnt, *singers in pds:
        for singer in range(cnt - 1):
            graph[singers[singer]].append(singers[singer + 1])
            priority[singers[singer + 1]] += 1

    answer = []
    for job, _ in enumerate(priority[1:], start=1):
        if not priority[job]:
            answer.append(job)
            queue.append(job)

    while queue:
        job = queue.popleft()
        for next_job in graph[job]:
            priority[next_job] -= 1
            if not priority[next_job]:
                answer.append(next_job)
                queue.append(next_job)

    if len(answer) != n:
        print(0)
    else:
        for ans in answer:
            print(ans)

n, m = map(int, input().split())
pds = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, pds)