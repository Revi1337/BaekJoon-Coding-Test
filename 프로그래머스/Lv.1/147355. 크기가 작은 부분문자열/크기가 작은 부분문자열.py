def solution(t, p):
    answer = 0
    length = len(p)
    for idx in range(length , len(t) + 1):
        p = int(p)
        tmp = t[idx - length : idx]
        if int(tmp) <= p:
            answer += 1
    return answer