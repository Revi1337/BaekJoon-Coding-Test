# 2026-03-13
# https://www.acmicpc.net/problem/9663
# backtrack

def solution(N):

    def backtrack(srow, scol):
        if srow == N:
            nonlocal ans
            ans += 1
            return

        for ncol in range(scol, N):
            if ch1[srow] == ch2[ncol] == ch3[srow + ncol] == ch4[srow - ncol] == 0:
                ch1[srow] = ch2[ncol] = ch3[srow + ncol] = ch4[srow - ncol] = 1
                backtrack(srow + 1, scol)
                ch1[srow] = ch2[ncol] = ch3[srow + ncol] = ch4[srow - ncol] = 0

    ch1, ch2 = [[0] * N for _ in range(2)]
    ch3, ch4 = [[0] * (N * 2) for _ in range(2)]
    ans = 0
    backtrack(0, 0)

    return ans

N = int(input())
print(solution(N))
