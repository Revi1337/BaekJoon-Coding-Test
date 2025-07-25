def solution(N, ranks):
    ranks.sort()
    ans, mn = 0, N + 1
    for _, r2 in ranks:
        if r2 < mn:
            mn = r2
            ans += 1
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, ranks))