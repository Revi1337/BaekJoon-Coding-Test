import sys

input = sys.stdin.readline

def solution(N, times):
    times.sort(key = lambda x: (x[1], x[0]))
    prev = times[0]
    answer = 1
    for idx in range(1, N):
        st, end = times[idx]
        if prev[1] <= st <= end:
            prev = times[idx]
            answer += 1
    return answer

N = int(input().rstrip())
times = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, times))
