import sys

input = sys.stdin.readline

def solution(N, vals):
    vals.sort()
    tmp = []
    for idx in range(N):
        cnt = 0
        for nv in range(vals[idx], vals[idx] + 5):
            if nv not in vals:
                cnt += 1
        tmp.append(cnt)
    return min(tmp)

N = int(input())
vals = [int(input()) for _ in range(N)]
print(solution(N, vals))
