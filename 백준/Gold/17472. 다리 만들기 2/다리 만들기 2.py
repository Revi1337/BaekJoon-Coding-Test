import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    def labeling():
        nodes, carr = [], [[0] * M for _ in range(N)]
        label = 1
        for row in range(N):
            for col in range(M):
                if arr[row][col] and not carr[row][col]:
                    stack = [[row, col]]
                    carr[row][col] = label
                    ns = []
                    while stack:
                        r, c = stack.pop()
                        ns.append([r, c])
                        for d in range(4):
                            nr, nc = r + drow[d], c + dcol[d]
                            if inside(nr, nc) and not carr[nr][nc] and arr[nr][nc] == 1:
                                carr[nr][nc] = label
                                stack.append([nr, nc])
                    nodes.append(ns)
                    label += 1

        return carr, nodes, label - 1

    def get_edges(nodes, carr):
        edges = []
        for nn in nodes:
            label = carr[nn[0][0]][nn[0][1]]
            for row, col in nn:
                for d in range(4):
                    dist, nrow, ncol = 0, row + drow[d], col + dcol[d]
                    while inside(nrow, ncol) and arr[nrow][ncol] == 0:
                        dist += 1
                        nrow, ncol = nrow + drow[d], ncol + dcol[d]
                    if inside(nrow, ncol) and arr[nrow][ncol] == 1:
                        other = carr[nrow][ncol]
                        if other != label and dist >= 2:
                            edges.append([dist, label, other])
        return edges

    def find(n):
        if parents[n] == n:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 != root2:
            parents[root2] = root1
            return True

        return False

    carr, nodes, cnt = labeling()
    edges = get_edges(nodes, carr)
    parents = list(range(cnt + 1))

    edges.sort()
    ans = 0
    for c, n1, n2 in edges:
        if union(n1, n2):
            ans += c

    root = find(1)
    for n in range(1, cnt + 1):
        if find(n) != root:
            return -1

    return ans

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, arr))