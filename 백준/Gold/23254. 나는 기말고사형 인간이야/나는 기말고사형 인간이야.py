import heapq

def solution(N, M, A, B):
    time, answer, pq = 24 * N, 0, []
    for idx in range(M):
        heapq.heappush(pq, [-B[idx], A[idx]])

    while pq and time != 0:
        unit, score = heapq.heappop(pq)
        unit = -unit
        while unit + score <= 100:
            if time > 0:
                score += unit
                time -= 1
            else:
                break
        if score == 100:
            answer += 100
        else:
            heapq.heappush(pq, [-(100 - score), score])

    answer += sum([score for _, score in pq])

    return answer

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(N, M, A, B))