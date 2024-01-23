import math

def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    left = [math.ceil((100 - progresses[idx]) / speeds[idx]) for idx in range(length)]
    max_day = left[0]
    cnt = 0
    for day in left:
        if day <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_day = day
    answer.append(cnt)
    return answer