def solution(idx, N):
    N.sort()
    return f'#{idx} {sum(N[1:-1]) / len(N[1:-1]):.0f}'

T = int(input())
for idx in range(T):
    N = list(map(int, input().split()))
    print(solution(idx + 1, N))