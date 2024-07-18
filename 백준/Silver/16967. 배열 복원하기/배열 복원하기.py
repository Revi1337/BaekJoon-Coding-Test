import sys

input = sys.stdin.readline

def solution(H, W, X, Y, B):
    for row in range(X, H):
        for col in range(Y, W):
            B[row][col] = B[row][col] - B[row - X][col - Y]
    for result in B[:H]:
        print(*result[:W])

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]
solution(H, W, X, Y, B)
