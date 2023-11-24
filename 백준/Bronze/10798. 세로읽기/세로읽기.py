def solution(datas: list):
    max_length = 0
    for data in datas:
        if len(data) > max_length:
            max_length = len(data)
    answer = ''
    for i in range(max_length):
        for j in range(len(datas)):
            if i < len(datas[j]):
              answer += datas[j][i]
    return answer

datas = [input() for _ in range(5)]
print(solution(datas))