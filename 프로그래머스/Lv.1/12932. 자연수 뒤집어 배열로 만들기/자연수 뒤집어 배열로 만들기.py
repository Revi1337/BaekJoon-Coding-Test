def solution(n):
    answer = []
    n = str(n)
    for idx in range(len(n) - 1, -1, -1):
        answer.append(int(n[idx]))
    return answer