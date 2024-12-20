def solution(N, K, A):

    def backtracking(n, sm):
        nonlocal answer
        if sm > K:
            return
        if n == N:
            if sm == K:
                answer += 1
            return
        backtracking(n + 1, sm + A[n])
        backtracking(n + 1, sm)

    answer = 0
    backtracking(0, 0)

    return answer


T = int(input())
for seq in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, K, A)}')