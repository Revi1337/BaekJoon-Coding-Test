def solution(N, A, OP):

    def backtrack(n, sm):
        if n == N - 1:
            nonlocal mn, mx
            mn, mx = min(mn, sm), max(mx, sm)
            return

        for idx in range(4):
            if OP[idx]:
                OP[idx] -= 1
                if idx == 0:
                    backtrack(n + 1, sm + A[n + 1])
                elif idx == 1:
                    backtrack(n + 1, sm - A[n + 1])
                elif idx == 2:
                    backtrack(n + 1, sm * A[n + 1])
                else:
                    backtrack(n + 1, int(sm / A[n + 1]))
                OP[idx] += 1

    mn, mx = 1_000_000_000, -1_000_000_000
    backtrack(0, A[0])

    print(mx, mn, sep = '\n')

N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))
solution(N, A, OP)
