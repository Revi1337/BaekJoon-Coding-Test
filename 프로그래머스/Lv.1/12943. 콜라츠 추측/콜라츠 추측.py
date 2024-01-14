def solution(num):
    answer = 0
    if num == 1:
        return 0
    data = num
    while data > 0:
        if answer >= 500:
            return -1
        if data % 2:
            data //= 2
        else:
            data = data * 3 + 1
        answer += 1
    return answer
