import sys

sys.setrecursionlimit(10000)

drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(w, h, datas):

    def DFS(row, col):
        datas[row][col] = 0
        for d in range(8):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (
                    (0 <= nrow < h)
                    and
                    (0 <= ncol < w)
                    and
                    (datas[nrow][ncol] != 0)
            ):
                DFS(nrow, ncol)

    answer = 0
    for row in range(h):
        for col in range(w):
            if datas[row][col] == 1:
                answer += 1
                DFS(row, col)

    return answer

input = sys.stdin.readline
while True:
    w, h = map(int, input().rstrip().split())
    if [w, h] == [0,0]:
        break
    datas = [list(map(int, input().rstrip().split())) for _ in range(h)]
    print(solution(w, h, datas))
