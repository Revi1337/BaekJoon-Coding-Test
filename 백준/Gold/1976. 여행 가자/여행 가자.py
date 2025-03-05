def solution(N, M, board, trace):

    def find(n):
        if parent[n] == n:
            return n

        parent[n] = find(parent[n])
        return parent[n]

    def union(n1, n2):
        rootA = find(n1)
        rootB = find(n2)
        if rootA != rootB:
            parent[rootA] = rootB

    parent = [i for i in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                union(i, j)

    root = find(trace[0])
    for city in trace[1:]:
        if find(city) != root:
            return "NO"

    return "YES"


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
trace = list(map(lambda x: x - 1, map(int, input().split())))
print(solution(N, M, board, trace))