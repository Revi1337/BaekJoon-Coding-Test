import sys

sys.setrecursionlimit(10 ** 6)

def solution(N, R, Q, E, ques):

    def make_tree(n, p):
        for cn in tree[n]:
            if cn != p:
                P[cn] = n
                C[n].append(cn)
                make_tree(cn, n)

    def count_child(n):
        tot = 0
        for cn in C[n]:
            tot += count_child(cn)

        DP[n] += tot
        return DP[n]

    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    P, C = [0] * (N + 1), [[] for _ in range(N + 1)]
    make_tree(R, -1)

    DP = [1] * (N + 1)
    count_child(R)
    print(*[DP[n] for n in ques], sep = '\n')

N, R, Q = map(int,sys.stdin.readline().rstrip().split())
E = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N - 1)]
ques = [int(sys.stdin.readline()) for _ in range(Q)]
solution(N, R, Q, E, ques)
