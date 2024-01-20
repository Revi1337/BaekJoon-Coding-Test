def solution(s1, s2):
    answer = 0
    for char in s1:
        for c in s2:
            if char == c:
                answer += 1
    return answer