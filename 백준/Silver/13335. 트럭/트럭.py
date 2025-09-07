import sys
from collections import deque

input = sys.stdin.readline

def solution(N, W, L, T):
    T.reverse()
    bridge = deque([0] * W)
    ans = sm = 0
    while bridge:
        ans += 1
        sm -= bridge.popleft()
        if T:
            if sm + T[-1] <= L:
                poped = T.pop()
                bridge.append(poped)
                sm += poped
            else:
                bridge.append(0)

    return ans

N, W, L = map(int, input().split())
T = list(map(int, input().split()))
print(solution(N, W, L, T))