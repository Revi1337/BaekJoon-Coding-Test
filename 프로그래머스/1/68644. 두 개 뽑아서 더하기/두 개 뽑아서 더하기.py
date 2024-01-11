def solution(datas):
    answer = []
    length = len(datas)
    for idx in range(length):
        for i in range(idx + 1, length):
            answer.append(datas[idx] + datas[i])
    return sorted(set(answer))