import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda row, col : 0 <= row < N and 0 <= col < N

    def backtrack(cnt, lst, check):
        if cnt == 3:
            poss.append([*lst])
            return
        for row in range(N):
            for col in range(N):
                if not check[row][col]:
                    check[row][col] = 1
                    lst.append([row, col])
                    backtrack(cnt + 1, lst, check)
                    lst.pop()
                    check[row][col] = 0

    poss = []
    backtrack(0, [], [[0] * (N + 1) for _ in range(N + 1)])

    ans = 200 * (10 ** 2)
    for lst in poss:
        check = {(lst[0][0], lst[0][1]), (lst[1][0], lst[1][1]), (lst[2][0], lst[2][1])}
        sm, possbile = sum(arr[row][col] for row, col in lst), True
        for row, col in lst:
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not inside(nrow, ncol) or (nrow, ncol) in check:
                    possbile = False
                    break
                check.add((nrow, ncol))
                sm += arr[nrow][ncol]
        if possbile:
            ans = min(ans, sm)

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))