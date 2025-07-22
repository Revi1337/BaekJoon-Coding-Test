def solution(N, M, W, T):
    W.sort()
    cnt = 0
    for prefix in T:
        left, right = 0, N - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if W[mid].startswith(prefix):
                found = True
                break
            elif W[mid] < prefix:
                left = mid + 1
            else:
                right = mid - 1
        if found:
            cnt += 1
    return cnt


N, M = map(int, input().split())
W = [input().rstrip() for _ in range(N)]
T = [input().rstrip() for _ in range(M)]
print(solution(N, M, W, T))
