import sys

input = sys.stdin.readline

def solution(lst):

    def w(a, b, c):
        if memo[a][b][c]:
            return memo[a][b][c]
        if a <= 0 or b <= 0 or c <= 0:
            memo[a][b][c] = 1
            return memo[a][b][c]
        if a > 20 or b > 20 or c > 20:
            memo[a][b][c] = w(20, 20, 20)
            return memo[a][b][c]
        if a < b < c:
            memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return memo[a][b][c]

        memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[a][b][c]

    memo = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    memo[0][0][0] = 1

    for a, b, c in lst:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

lst = []
while True:
    a, b, c = map(int, input().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        solution(lst)
        break
    lst.append([a, b, c])