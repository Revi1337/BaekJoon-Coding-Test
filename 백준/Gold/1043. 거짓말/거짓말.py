def solution(N, M, kcnt, know, parties):
    answer = []
    know, parties = set(know), [set(party) for party in parties]

    for _ in range(M):
        cnt = 0
        for party in parties:
            if know & party:
                know = know.union(party)
            else:
                cnt += 1
        answer.append(cnt)

    return min(answer)

N, M = map(int, input().split())
k = list(map(int, input().split()))
kcnt, know = k[0], k[1:]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]
print(solution(N, M, kcnt, know, parties))
