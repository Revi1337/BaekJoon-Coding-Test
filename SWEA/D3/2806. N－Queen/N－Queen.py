def solution(seq, N):

    answer = 0
    v1, v2, v3 = [[0] * (2 * N) for _ in range(3)] # [0, 0, 0, 0, 0, 0] 을 3 개 초기화하여 Unpack

    def dfs(queen):
        if queen == N:
            nonlocal answer
            answer += 1
            return
        for col in range(N):
            if v1[col] == v2[queen + col] == v3[queen - col] == 0:
                v1[col] = v2[queen + col] = v3[queen - col] = 1
                dfs(queen + 1)
                v1[col] = v2[queen + col] = v3[queen - col] = 0 # 원상 복구

    dfs(0)

    return f'#{seq} {answer}'

T = int(input())
for seq in range(T):
    N = int(input())
    print(solution(seq + 1, N))
