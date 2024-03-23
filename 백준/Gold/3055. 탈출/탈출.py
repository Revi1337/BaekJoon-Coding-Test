from collections import deque
import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(r, c, field):

    queue = deque()
    check = [[0] * c for _ in range(r)]
    end_row = end_col = None

    for row in range(r):
        for col in range(c):
            if field[row][col] == 'S':
                queue.append((row, col))
            elif field[row][col] == 'D':
                end_row, end_col = row, col

    for row in range(r):
        for col in range(c):
            if field[row][col] == '*':
                queue.append((row, col))

    while queue:                        # 고슴도치, 물 순서
        row, col = queue.popleft()
        if field[end_row][end_col] == 'S':
            return check[end_row][end_col]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if (0 <= nrow < r) and (0 <= ncol < c):
                if (field[nrow][ncol] == '.' or field[nrow][ncol] == 'D') and (field[row][col] == 'S'): # (현재지점이 S) 이고 (다음 지점이 . 혹은 D) 이면
                    field[nrow][ncol] = 'S'                 # 다음지점으로 고슴도치가 이동한다.
                    check[nrow][ncol] = check[row][col] + 1 # 다음지점의 횟수는 이전지점 + 1
                    queue.append((nrow, ncol))              # queue 에 다음지점을 넣는다.
                elif (field[nrow][ncol] == '.' or field[nrow][ncol] == 'S') and (field[row][col] == '*'): # (현재지점이 *) 이고 (다음지점이 . 혹은 S) 이면
                    field[nrow][ncol] = '*'                 # 다음지점에 물을전파시키고
                    queue.append((nrow, ncol))              # 큐에 다음지점을 넣는다.
    return 'KAKTUS'

r, c = map(int, input().split())
field = [list(input().rstrip()) for _ in range(r)]
print(solution(r, c, field))
