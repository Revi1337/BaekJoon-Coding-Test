def solution(N, M, cards):
    possible = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                cost = cards[i] + cards[j] + cards[k]
                if cost <= M:
                    possible.append(cost)

    return max(possible)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(N, M, cards))
