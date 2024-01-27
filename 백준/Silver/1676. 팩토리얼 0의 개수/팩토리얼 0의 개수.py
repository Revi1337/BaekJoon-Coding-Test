def solution(num):
    integer = 1
    for number in range(1, num + 1):
        integer *= number
    integer = str(integer)
    answer = 0
    for idx in range(len(integer) - 1, -1, -1):
        if integer[idx] == '0':
            answer += 1
        else:
            return answer
    return answer

number = int(input())
print(solution(number))
