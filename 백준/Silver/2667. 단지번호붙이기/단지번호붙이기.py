drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, maps):

    counter = 0

    def dfs(row, col):
        nonlocal counter
        counter += 1
        maps[row][col] = 0
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < n) and (maps[nrow][ncol]):
                dfs(nrow, ncol)

    answer = []
    for row in range(n):
        for col in range(n):
            if maps[row][col]:
                dfs(row, col)
                answer.append(counter)
                counter = 0

    print(len(answer))
    for cnt in sorted(answer):
        print(cnt)

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
solution(n, maps)
