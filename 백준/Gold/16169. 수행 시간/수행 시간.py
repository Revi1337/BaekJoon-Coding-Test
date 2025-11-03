import sys

input = sys.stdin.readline

def solution(N, C):
    lvs, spds = [[0] * (N + 1) for _ in range(2)]
    for idx in range(1, N + 1):
        lvs[idx], spds[idx] = C[idx - 1]

    ans = [0] * (N + 1)
    for idx in range(1, N + 1):
        if lvs[idx] == 1:
            ans[idx] = spds[idx]

    mx = max(lvs)
    for lv in range(2, mx + 1):
        ps = [idx for idx in range(1, N + 1) if lvs[idx] == lv - 1]
        cs = [idx for idx in range(1, N + 1) if lvs[idx] == lv]
        for cn in cs:
            st = 0
            for pn in ps:
                st = max(st, ans[pn] + (cn - pn) ** 2)
            ans[cn] = st + spds[cn]

    return max(ans)

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, C))
