def solution(N, P, R):

    def delete(n):
        P[n] = -100
        for nn in tree[n]:
            delete(nn)

    root, tree = None, [[] for _ in range(N)]
    for ch, p in enumerate(P):
        if p != -1:
            tree[p].append(ch)

    delete(R)
    ans = 0
    for n in range(N):
        if P[n] != -100 and n not in P:
            ans += 1

    return ans

N = int(input())
P = list(map(int, input().split()))
R = int(input())
print(solution(N, P, R))