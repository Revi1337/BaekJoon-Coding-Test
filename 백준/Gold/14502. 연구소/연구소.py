# 2026-03-13
# https://www.acmicpc.net/problem/14502
# backtrack + bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    EMPTY, WALL, VIRUS = 0, 1, 2

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    def spread():
        queue = deque(virus)
        carr = [[*line] for line in arr]

        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol) and not carr[nrow][ncol]:
                    carr[nrow][ncol] = VIRUS
                    queue.append([nrow, ncol])

        cnt = 0
        for row in range(N):
            for col in range(M):
                if carr[row][col] == 0:
                    cnt += 1

        return cnt


    def build_wall(st, cnt):
        if cnt == 3:
            nonlocal ans
            cnt = spread()
            ans = max(ans, cnt)
            return

        for nxt in range(st, len(poss)):
            arr[poss[nxt][0]][poss[nxt][1]] = WALL
            build_wall(nxt + 1, cnt + 1)
            arr[poss[nxt][0]][poss[nxt][1]] = EMPTY

    poss, virus = [], []
    for row in range(N):
        for col in range(M):
            if arr[row][col] == EMPTY:
                poss.append([row, col])
            elif arr[row][col] == VIRUS:
                virus.append([row, col])

    ans = 0
    build_wall(0, 0)

    return ans

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, arr))
