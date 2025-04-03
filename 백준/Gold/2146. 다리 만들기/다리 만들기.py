from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    check = [[0] * N for _ in range(N)]
    sequence = 1
    edges = []
    for row in range(N):
        for col in range(N):
            if board[row][col] and not check[row][col]:
                check[row][col] = sequence
                queue = deque([(row, col)])
                edge = set()
                while queue:
                    sr, sc = queue.popleft()
                    for d in range(4):
                        nr, nc = sr + drow[d], sc + dcol[d]
                        if inside(nr, nc):
                            if not board[nr][nc]:
                                edge.add((sr, sc))
                            else:
                                if not check[nr][nc]:
                                    check[nr][nc] = sequence
                                    queue.append((nr, nc))
                if edge:
                    edges.append(edge)
                sequence += 1

    # 섬 사이에 다른 섬이 껴있을수도 있음. 따라서 맨헤튼 거리는 불가. BFS 를 돌려야함.
    answer = 1e9
    for sequence, edge in enumerate(edges, start = 1):
        queue = deque([(row, col, 0) for row, col in edge])
        visit = [[0] * N for _ in range(N)]
        while queue:
            row, col, cnt = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol):
                    if not check[nrow][ncol]:
                        if not visit[nrow][ncol]:
                            visit[nrow][ncol] = 1
                            queue.append((nrow, ncol, cnt + 1))
                    else:
                        if check[nrow][ncol] != sequence:
                            answer = min(answer, cnt)

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
