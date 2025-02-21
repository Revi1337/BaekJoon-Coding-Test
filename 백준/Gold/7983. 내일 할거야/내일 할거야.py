def solution(N, jobs):
    jobs.sort(key=lambda x: -x[1])

    last = float('inf')
    for d, t in jobs:
        last = min(last, t)
        last -= d

    return last


N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, jobs))