def solution(left, right):
    answer = 0
    numbers = [val for val in range(left, right + 1)]
    for number in numbers:
        if number == 1:
            answer -= 1
            continue
        cnt = 2
        for integer in range(2, number // 2 + 1):
            if not number % integer:
                cnt += 1
        if cnt % 2:
            answer -= number
        else:
            answer += number
    return answer
