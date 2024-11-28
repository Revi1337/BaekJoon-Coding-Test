def solution(L, N, users):
    ex = 0
    for idx in range(N):
        if users[idx][1] - users[idx][0] > users[ex][1] - users[ex][0]:
            ex = idx
    ex += 1

    cakes = [0] * (L + 1)
    for idx in range(N):
        v1, v2 = users[idx]
        for seq in range(v1, v2 + 1):
            if not cakes[seq]:
                cakes[seq] = idx + 1

    counter = [0] * (N + 1)
    for c in cakes:
        if c:
            counter[c - 1] += 1

    answer = counter.index(max(counter))

    print(ex, answer + 1, sep = ' ')


L = int(input())
N = int(input())
users = [list(map(int, input().split())) for _ in range(N)]
solution(L, N, users)