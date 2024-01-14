def solution(absolutes, signs):
    length = len(absolutes)
    answer = 0
    for idx in range(length):
        if signs[idx]:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
    return answer
        