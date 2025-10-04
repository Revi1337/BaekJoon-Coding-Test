def solution(N):
    ans = 1
    while N != 1:
        if N % 2:
            ans += 1
            N -= 1
        else:
            N //= 2

    return ans