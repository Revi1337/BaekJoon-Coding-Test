def solution(N, M, cards):
    answer = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                cost = cards[i] + cards[j] + cards[k]
                if answer < cost <= M:
                    answer = cost

    return answer

N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(N, M, cards))
