import sys

input = sys.stdin.readline

def solution(n, scores):

    def round(n):
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)

    if n == 0:
        return 0
    scores.sort()
    padding = round(n * 0.15)
    return round(sum(scores[padding : n - padding]) / (n - padding * 2))

n = int(input().rstrip())
scores = [int(input().rstrip()) for _ in range(n)]
print(solution(n, scores))