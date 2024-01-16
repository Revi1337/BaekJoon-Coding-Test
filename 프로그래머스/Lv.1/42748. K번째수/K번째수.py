def solution(array, commands):
    answer = []
    for i, j, k in commands:
        tmp = array[i - 1 : j]
        answer.append(sorted(tmp)[k - 1])
    return answer