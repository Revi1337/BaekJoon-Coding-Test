def solution(N, D, K, C, foods):
    cache = [0] * (D + 1)
    cnt = 0
    for idx in range(K):
        if cache[foods[idx]] == 0:
            cnt += 1
        cache[foods[idx]] += 1
    answer = cnt
    if cache[C] == 0:
        answer += 1

    for idx in range(N):
        cache[foods[idx]] -= 1
        if cache[foods[idx]] == 0:
            cnt -= 1

        right = (idx + K) % N
        if cache[foods[right]] == 0:
            cnt += 1
        cache[foods[right]] += 1

        current_distinct = cnt
        if cache[C] == 0:
            current_distinct += 1

        answer = max(answer, current_distinct)

    return answer

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
print(solution(N, d, k, c, belt))
