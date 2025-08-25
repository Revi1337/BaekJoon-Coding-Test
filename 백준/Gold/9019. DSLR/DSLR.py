import sys
from collections import deque

input = sys.stdin.readline

def solution(A, B):

    def D(cost): return 2 * cost % 10000

    def S(cost): return 9999 if cost == 0 else cost - 1

    def L(cost): return (cost % 1000) * 10 + (cost // 1000)

    def R(cost): return (cost // 10) + (cost % 10) * 1000

    sign, trace = [''] * 10001, [-1] * 10001
    functions, mapper = [D, S, L, R], ['D', 'S', 'L', 'R']
    queue = deque([[A, A]])
    trace[A] = A

    while queue:
        cost, bcost = queue.popleft()
        if cost == B:
            ans = []
            while cost != A:
                ans.append(sign[cost])
                cost = trace[cost]
            return "".join(ans[::-1])

        for idx in range(4):
            ncost = functions[idx](cost)
            if trace[ncost] != -1:
                continue
            sign[ncost], trace[ncost] = mapper[idx], cost
            queue.append([ncost, cost])

T = int(input())
for _ in range(T):
    A, B = map(int, input().rstrip().split())
    print(solution(A, B))
