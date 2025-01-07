# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def solution(N, M, R, arr):
    def rotate_layer(padding):
        d, sr, sc = 0, padding, padding
        prev = arr[sr][sc]
        er, ec = sr, sc
        while True:
            nr, nc = sr + dr[d], sc + dc[d]
            if not (padding <= nr < N - padding and padding <= nc < M - padding):
                d = (d + 1) % 4
                continue
            arr[nr][nc], prev = prev, arr[nr][nc]
            sr, sc = nr, nc
            if (sr, sc) == (er, ec):
                break

    for padding in range(min(N, M) // 2):
        layer_size = 2 * ((N - 2 * padding) + (M - 2 * padding) - 2)
        actual_rotations = R % layer_size
        for _ in range(actual_rotations):
            rotate_layer(padding)

    for line in arr:
        print(*line)

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, R, arr)