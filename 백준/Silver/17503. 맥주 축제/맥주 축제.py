def solution(N, M, K, beers):
    beers.sort(reverse=True)
    left, right = 0, 2 ** 31
    while left <= right:
        mid = (left + right) // 2
        cnt = sm = 0
        for p, lv in beers:
            if lv <= mid:
                cnt += 1
                sm += p
            if cnt == N:
                break

        if sm >= M and cnt == N:
            right = mid - 1
        else:
            left = mid + 1

    return left if right != 2 ** 31 else -1

N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]
print(solution(N, M, K, beers))