import sys

input = sys.stdin.readline

directions = (0, 1), (-1, 0), (0, -1), (1, 0)

def solution(M, N, operations):
    curr = [0, 0]
    answer = [[*curr]]
    d = 0
    for operation in operations:
        command, value = operation[0], int(operation[1])
        if command == 'TURN':
            if value == 0:
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
        else:
            nrow = curr[0] + (directions[d][0] * value)
            ncol = curr[1] + (directions[d][1] * value)
            if nrow < 0 or nrow > M or ncol < 0 or ncol > M:
                print(-1)
                return
            curr[0] = nrow
            curr[1] = ncol
            answer.append([curr[1], curr[0]])

    print(*answer[-1], sep = ' ')



M, N = map(int, input().split())
operations = [input().strip().split() for _ in range(N)]
solution(M, N, operations)

