from collections import deque

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def solution(N, K, A, L, D):
    answer = dir = 0
    tdic = {int(t): d for t, d in D}
    A = set((row, col) for row, col in A)

    S = deque([(1, 1)])
    while True:
        answer += 1
        row, col = S[-1]

        nrow, ncol = row + drow[dir], col + dcol[dir]
        if not (1 <= nrow <= N and 1 <= ncol <= N):
            return answer
        if (nrow, ncol) in S:
            return answer

        S.append((nrow, ncol))
        if (nrow, ncol) not in A:
            S.popleft()
        else:
            A.discard((nrow, ncol))

        if answer in tdic:
            if tdic[answer] == 'L':
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4

N = int(input())
K = int(input())
A = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
D = [input().split() for _ in range(L)]
print(solution(N, K, A, L, D))
