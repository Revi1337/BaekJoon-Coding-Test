from collections import deque

# 시계방향 (상, 우, 하, 좌) 순
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

# (하, 좌, 상, 우) 순
direction = {
    1: [[1,2,4,7], [1,3,4,5], [1,2,5,6], [1,3,6,7]],
    2: [[1,2,4,7], [], [1,2,5,6], []],
    3: [[], [1,3,4,5], [], [1,3,6,7]],
    4: [[], [], [1,2,5,6], [1,3,6,7]],
    5: [[1,2,4,7], [], [], [1,3,6,7]],
    6: [[1,2,4,7], [1,3,4,5], [], []],
    7: [[], [1,3,4,5], [1,2,5,6], []]
}

def solution(N, M, R, C, L, maps):

    answer = 0
    nmaps = [[0] * M for _ in range(N)]
    nmaps[R][C] = 1
    queue = deque([(R, C)])

    while queue:
        row, col = queue.popleft()
        if 0 < nmaps[row][col] <= L:
            answer += 1
        elif nmaps[row][col] != 0 and nmaps[row][col] > L:
            break
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if (0 <= nrow < N) and (0 <= ncol < M) and (maps[nrow][ncol] != 0) and (nmaps[nrow][ncol] == 0):
                for poss in direction[maps[nrow][ncol]][d]:
                    if maps[row][col] == poss:
                        nmaps[nrow][ncol] = nmaps[row][col] + 1
                        queue.append((nrow, ncol))
                        break

    return answer

T = int(input())
for seq in range(T):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, M, R, C, L, maps)}')
