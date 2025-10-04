def solution(N, A, B):
    ans = 0
    while A != B:
        A = (A + 1) // 2
        B = (B + 1) // 2
        ans += 1

    return ans