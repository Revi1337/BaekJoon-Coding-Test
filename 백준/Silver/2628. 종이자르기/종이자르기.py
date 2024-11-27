def solution(N, M, C, edges):
    paper = [[1] * M for _ in range(N)]
    redges, cedges = [], []
    for type, line in edges:
        if type == 0:
            redges.append(line)
        else:
            cedges.append(line)

    redges = sorted(set(redges))
    for idx in range(len(redges)):
        paper.insert(redges[idx] + idx, [0] * M)

    paper = list(map(list, zip(*paper)))
    length = len(paper[0])
    cedges = sorted(set(cedges))
    for idx in range(len(cedges)):
        paper.insert(cedges[idx] + idx, [0] * length)

    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    def dfs(r, c):
        nonlocal counter
        counter += 1
        check[r][c] = 1
        for d in range(4):
            nrow, ncol = r + drow[d], c + dcol[d]
            if 0 <= nrow < row_len and 0 <= ncol < col_len:
                if paper[nrow][ncol] and not check[nrow][ncol]:
                    dfs(nrow, ncol)

    answer = []
    row_len, col_len = len(paper), len(paper[0])
    check = [[0] * col_len for _ in range(row_len)]
    for row in range(row_len):
        for col in range(col_len):
            if paper[row][col] and not check[row][col]:
                counter = 0
                dfs(row, col)
                answer.append(counter)

    return max(answer)

M, N = map(int, input().split())
C = int(input())
edges = [list(map(int, input().split())) for _ in range(C)]
print(solution(N, M, C, edges))