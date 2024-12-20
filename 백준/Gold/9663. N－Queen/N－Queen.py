def solution(N):

    def backtracking(n):
        if n == N:
            nonlocal answer
            answer += 1
            return
        for col in range(N):
            if rows[col] == 0 and digon1[n + col] == 0 and digon2[n - col] == 0:
                rows[col] = digon1[n + col] = digon2[n - col] = 1
                backtracking(n + 1)
                rows[col] = digon1[n + col] = digon2[n - col] = 0

    rows = [0] * N
    digon1 = [0] * (2 * N)
    digon2 = [0] * (2 * N)

    answer = 0
    backtracking(0)

    return answer

N = int(input())
print(solution(N))