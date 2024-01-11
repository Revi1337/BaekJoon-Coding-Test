def solution(k, score):
    answer = []
    mutable = []
    for day in range(len(score)):
        if day < k:
            mutable.append(score[day])
        elif score[day] > min(mutable):
            mutable.remove(min(mutable))
            mutable.append(score[day])
        answer.append(min(mutable))

    return answer