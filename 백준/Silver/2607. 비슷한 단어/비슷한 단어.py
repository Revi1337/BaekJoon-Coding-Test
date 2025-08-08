def solution(N, S):
    init, ans = S[0], 0
    for s in S[1:]:
        ichars, cnt = list(init), 0
        for char in s:
            if char in ichars:
                ichars.remove(char)
            else:
                cnt += 1
        if cnt < 2 and len(ichars) < 2:
            ans += 1

    return ans

N = int(input())
S = [input().rstrip() for _ in range(N)]
print(solution(N, S))
