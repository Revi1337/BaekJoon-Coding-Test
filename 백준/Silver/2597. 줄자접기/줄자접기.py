import sys

input = sys.stdin.readline

"""
줄자 접기 (https://www.acmicpc.net/problem/2597)
2024-09-10
"""

def solution(N, colors):
    llen = 0
    rlen = N
    for idx in range(3):
        color = colors[idx]
        if color[0] == color[1]:
            continue
        mid = sum(color) / 2
        llen, rlen = min(llen, mid * 2 - rlen), mid
        for i in range(idx + 1, 3):
            for k in range(2):
                if colors[i][k] > mid:
                    colors[i][k] = mid * 2 - colors[i][k]

    return '{:.01f}'.format(rlen - llen)

N = int(input())
colors = [list(map(int, input().split())) for _ in range(3)]
print(solution(N, colors))
