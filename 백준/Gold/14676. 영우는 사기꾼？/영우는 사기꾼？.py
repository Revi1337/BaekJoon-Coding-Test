def solution(N, M, K, E, G):
    dag = [[] for _ in range(N + 1)]
    ind, cnt = [[0] * (N + 1) for _ in range(2)]
    for v1, v2 in E:
        dag[v1].append(v2)
        ind[v2] += 1

    for op, n in G:
        if op == 1:
            if ind[n] > 0:
                return "Lier!"
            cnt[n] += 1
            if cnt[n] == 1:
                for nn in dag[n]:
                    ind[nn] -= 1
        else:
            if cnt[n] == 0:
                return "Lier!"
            cnt[n] -= 1
            if cnt[n] == 0:
                for nn in dag[n]:
                    ind[nn] += 1

    return "King-God-Emperor"

N, M, K = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
G = [list(map(int, input().split())) for _ in range(K)]
print(solution(N, M, K, E, G))