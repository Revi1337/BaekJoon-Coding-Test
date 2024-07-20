import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, costs, weights, seq):
    park = [0] * (N + 1)
    plength = len(park)
    costs.insert(0, 0)
    weights.insert(0, 0)
    seq = deque(seq)
    pending = deque()
    answer = 0
    while seq:
        car = seq.popleft()
        if car > 0:
            for p in range(1, plength):
                if not park[p]:
                    park[p] = car
                    break
            else:
                pending.append(car)
        else:
            for p in range(1, plength):
                if park[p] == (car * -1):
                    answer += (costs[p] * weights[car * -1])
                    park[p] = 0
                    if pending:
                        park[p] = pending.popleft()

    return answer

N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]
weights = [int(input()) for _ in range(M)]
seq = [int(input()) for _ in range(2 * M)]
print(solution(N, M, costs, weights, seq))

