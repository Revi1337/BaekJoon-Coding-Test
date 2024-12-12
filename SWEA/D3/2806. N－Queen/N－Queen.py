def solution(N):

    def backtracking(n):
        if n == N:
            nonlocal answer
            answer += 1
            return
        for idx in range(N):
            if v1[idx] == v2[n + idx] == v3[n - idx] == 0:
                v1[idx] = v2[n + idx] = v3[n - idx] = 1
                backtracking(n + 1)
                v1[idx] = v2[n + idx] = v3[n - idx] = 0

    answer = 0
    v1 = [0] * N
    v2 = [0] * (2 * N) # 좌하 -> 우상 대각선 (row + col)
    v3 = [0] * (2 * N) # 우상 -> 좌하 대각선 (row - col)
    backtracking(0)

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    print(f'#{seq + 1} {solution(N)}')