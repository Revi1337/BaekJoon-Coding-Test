def solution(i, N, K, scores):
    seed = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score = [0] * (N + 1)
    for idx, (s1, s2, s3) in enumerate(scores, start=1):
        score[idx] += s1 * 0.35
        score[idx] += s2 * 0.45
        score[idx] += s3 * 0.2

    target = score[K]
    sorted_total = sorted(score[1:], reverse=True)
    offset = N // 10
    answer = sorted_total.index(target) // offset
    return f'#{i} {seed[answer]}'

T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    print(solution(idx + 1, N, K, scores))