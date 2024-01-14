def solution(num):
    answer = 0
    if num == 1:
        return 0
    number = num
    while number > 1:
        if number % 2 == 1:
            number = (number * 3) + 1
        elif number % 2 == 0:
            number = number // 2
        answer += 1
        if answer == 500:
            return -1
    return answer

print(solution(626331))