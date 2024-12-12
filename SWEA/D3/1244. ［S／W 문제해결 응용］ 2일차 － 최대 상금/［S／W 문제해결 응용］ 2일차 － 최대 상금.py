def solution(N, M):

    N = list(str(N))
    length = len(N)

    def backtracking(n):
        if n == M:
            nonlocal answer
            answer = max(answer, int("".join(N)))
            return
        for i in range(length - 1):
            for j in range(i + 1, length):
                N[i], N[j] = N[j], N[i]
                chk = int("".join(N))
                if (n, chk) not in check:
                    backtracking(n + 1)
                    check.add((n, chk))
                N[i], N[j] = N[j], N[i]

    check = set()
    answer = -1e9
    backtracking(0)

    return answer

T = int(input())
for seq in range(T):
    N, M = map(int, input().split())
    print(f'#{seq + 1} {solution(N, M)}')

