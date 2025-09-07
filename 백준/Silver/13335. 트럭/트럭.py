import sys
from collections import deque

input = sys.stdin.readline

def solution(N, W, L, T):
    T.reverse()
    ans = 0
    bridge = deque([0] * W)
    while bridge:
        ans += 1
        bridge.popleft()
        if T:
            if sum(bridge) + T[-1] <= L:
                bridge.append(T.pop())
            else:
                bridge.append(0)

    return ans


N, W, L = map(int, input().split())
T = list(map(int, input().split()))
print(solution(N, W, L, T))
