def solution(N, B, S):

    def backtracking(n, sm):
        nonlocal answer
        if sm >= answer: # cut edge
            return

        if n == N:
            if sm >= B:
                answer = min(answer, sm)
            return
        backtracking(n + 1, sm + S[n])
        backtracking(n + 1, sm)

    answer = 1e9
    backtracking(0, 0)

    return answer - B

T = int(input())
for seq in range(T):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, B, S)}')