dir = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}

def solution(N, M, R, arr, Q):
    inside = lambda row, col : 0 <= row < N and 0 <= col < M

    state = [['S'] * M for _ in range(N)]
    ans = 0
    for idx in range(0, len(Q), 2):
        att, defen = Q[idx], Q[idx + 1]

        srow, scol, d = int(att[0]) - 1, int(att[1]) - 1, dir[att[2]]
        if state[srow][scol] == 'F':
            pass
        else:
            reach = arr[srow][scol]
            while inside(srow, scol) and reach > 0:
                if state[srow][scol] == 'S':
                    state[srow][scol] = 'F'
                    ans += 1
                    reach = max(reach, arr[srow][scol])
                reach -= 1
                srow += d[0]
                scol += d[1]

        drow, dcol = int(defen[0]) - 1, int(defen[1]) - 1
        if state[drow][dcol] == 'F':
            state[drow][dcol] = 'S'

    print(ans)
    for line in state:
        print(*line)

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = [list(input().rstrip().split()) for _ in range(R * 2)]
solution(N, M, R, arr, Q)
