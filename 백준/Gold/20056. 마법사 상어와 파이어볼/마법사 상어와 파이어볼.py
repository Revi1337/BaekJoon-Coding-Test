drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(N, M, K, balls):

    board = [[[] for _ in range(N)] for _ in range(N)]
    for idx in range(M):
        balls[idx][0] -= 1
        balls[idx][1] -= 1

    for _ in range(K):
        # 현재 balls 들의 다음 좌표를 계산해서 board 에 놔본다.
        while balls:
            r, c, m, s, d = balls.pop()
            nrow, ncol = r, c
            for _ in range(s):
                nrow, ncol = (nrow + drow[d]) % N, (ncol + dcol[d]) % N
            board[nrow][ncol].append([nrow, ncol, m, s, d])

        # board 를 순회하며, 공들을 쪼개고 다시 balls 에 append 한다.
        for row in range(N):
            for col in range(N):
                if not board[row][col]:
                    continue
                length = len(board[row][col])
                if length >= 2:
                    sumM = sumS = odd = even = 0
                    for r, c, m, s, d in board[row][col]:
                        if d % 2:
                            odd += 1
                        else:
                            even += 1
                        sumM += m
                        sumS += s
                    nm, ns = sumM // 5, sumS // length
                    if nm != 0:
                        if odd == length or even == length:
                            for d in [0,2,4,6]:
                                balls.append([row, col, nm, ns, d])
                        else:
                            for d in [1,3,5,7]:
                                balls.append([row, col, nm, ns, d])
                else:
                    balls.append(board[row][col][0])
                board[row][col].clear()

    answer = 0
    for r, c, m, s, d in balls:
        answer += m

    return answer

N, M, K = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, balls))
