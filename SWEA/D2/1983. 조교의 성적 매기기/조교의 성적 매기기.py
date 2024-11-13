grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

def solution(idx, N, K, scores):
    s_scores = [0] * (N + 1)
    for index, (mid, final, work) in enumerate(scores, start=1):
        s_scores[index] += mid * 0.35
        s_scores[index] += final * 0.45
        s_scores[index] += work * 0.20

    target = s_scores[K]
    ss_scores = sorted(s_scores[1:], reverse=True)
    offset = N // 10
    answer = ss_scores.index(target) // offset

    return f'#{idx} {grades[answer]}'

T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    print(solution(idx + 1, N, K, scores))