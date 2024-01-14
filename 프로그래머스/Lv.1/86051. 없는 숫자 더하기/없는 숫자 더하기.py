def solution(numbers):
    answer = 0
    datas = [0] * 10
    for idx in range(len(numbers)):
        datas[numbers[idx]] = 1
    for idx in range(10):
        if not datas[idx]:
            answer += idx
    return answer