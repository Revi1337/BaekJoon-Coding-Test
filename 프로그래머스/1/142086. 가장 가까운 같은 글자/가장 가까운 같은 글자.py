def solution(s):
    table = {}
    answer = []
    for idx in range(len(s)):
        if not s[idx] in table:
            answer.append(-1)
            table[s[idx]] = idx
        else:
            answer.append(idx - table[s[idx][-1]])
            table[s[idx]] = idx
    return answer