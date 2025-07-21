def solution(N, M, P):
    mn, mx = max(P), sum(P)
    ans = mx
    while mn <= mx:
        mid = (mn + mx) // 2
        total, cnt = mid, 1

        for cost in P:
            if total < cost:
                cnt += 1
                total = mid
            total -= cost

        if cnt <= M:
            ans = mid
            mx = mid - 1
        else:
            mn = mid + 1

    return ans

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]
print(solution(N, M, P))
