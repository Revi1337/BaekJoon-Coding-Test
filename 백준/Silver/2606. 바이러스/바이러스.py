import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, edges):
    graphs = [[] for _ in range(N + 1)]
    for v1, v2 in edges:
        graphs[v1].append(v2)
        graphs[v2].append(v1)

    def dfs(entry):
        nonlocal answer
        check[entry] = 1
        answer += 1
        for nv in graphs[entry]:
            if not check[nv]:
                dfs(nv)

    check = [0] * (N + 1)
    answer = 0
    dfs(1)
    return answer - 1

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, edges))