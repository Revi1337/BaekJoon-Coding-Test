from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, K, arr, S, X, Y):

    queue = deque(sorted((arr[row][col], row, col) for row in range(N) for col in range(N)))

    while S > 0:
        nqueue = []
        while queue:
            virus, row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < N:
                    if not arr[nrow][ncol]:
                        arr[nrow][ncol] = virus
                        nqueue.append((virus, nrow, ncol))

        queue = deque(sorted(nqueue))
        S -= 1

    return arr[X - 1][Y - 1] if arr[X - 1][Y - 1] else 0


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
print(solution(N, K, arr, S, X, Y))