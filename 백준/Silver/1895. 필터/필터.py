import sys

input = sys.stdin.readline

def solution(R, C, board, T):
    total = []
    for i in range(R - 2):
        for j in range(C - 2):
            arr = []
            for k in range(3):
                for l in range(3):
                    arr.append(board[i + k][j + l])
            arr.sort()
            total.append(arr[4])

    ans = 0
    for i in total:
        if i >= T:
            ans += 1
    return ans

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
T = int(input())
print(solution(R, C, board, T))