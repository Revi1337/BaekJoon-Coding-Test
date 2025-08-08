import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(arr):

    inside = lambda row, col : 0 <= row < SIZE and 0 <= col < SIZE

    SIZE, LIMIT = 5, 6
    poss = set()
    for row in range(SIZE):
        for col in range(SIZE):
            queue = deque([[row, col, str(arr[row][col])]])
            while queue:
                srow, scol, curr = queue.popleft()
                if len(curr) == LIMIT:
                    poss.add(curr)
                    continue
                for d in range(4):
                    nrow, ncol = srow + drow[d], scol + dcol[d]
                    if inside(nrow, ncol):
                        queue.append([nrow, ncol, curr + str(arr[nrow][ncol])])

    return len(poss)


arr = [list(map(int, input().split())) for _ in range(5)]
print(solution(arr))