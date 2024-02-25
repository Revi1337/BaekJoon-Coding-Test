import sys

def solution(n, graph):
    vertext_cnt = n
    answer = float('inf')

    def dfs(c_vertext, next_vertext, cost, check):
        nonlocal answer
        if len(check) == vertext_cnt:
            tmp = graph[next_vertext][c_vertext]
            if tmp != 0:
                answer = min(answer, cost + tmp)
            return

        for n_vertext in range(vertext_cnt):
            next_cost = graph[next_vertext][n_vertext]
            if (next_cost) and (n_vertext not in check) and (cost < answer):
                check.append(n_vertext)
                dfs(c_vertext, n_vertext, cost + next_cost, check)
                check.pop()

    for vertext in range(vertext_cnt):
        dfs(vertext, vertext, 0, [vertext])

    return answer

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, edges))
