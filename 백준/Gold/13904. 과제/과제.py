import sys

input = sys.stdin.readline

def solution(N, W):
    W.sort(key=lambda x: -x[1])
    mxd = max(d for d, w in W)
    check = [0] * (mxd + 1)
    ans = 0
    for d, w in W:
        for day in range(d, 0, -1):
            if not check[day]:
                check[day] = True
                ans += w
                break
    return ans

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, W))
