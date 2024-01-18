def solution(name, yearning, photo):
    answer = []
    scores = {}
    for idx in range(len(name)):
        if scores.get(name[idx]) is None:
            scores[name[idx]] = yearning[idx]
    for picture in photo:
        score = 0
        for human in picture:
            if human in scores:
                score += scores[human]
        answer.append(score)
    return answer