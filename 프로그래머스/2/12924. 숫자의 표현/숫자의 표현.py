def solution(n):
    ans = 1
    for num in range(1, (n // 2) + 1):
        sm = 0
        while sm < n:
            sm += num
            if sm == n:
                ans += 1
                break
            num += 1

    return ans