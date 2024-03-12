import sys

input = sys.stdin.readline

def solution(num1, num2):
    if num1 == num2:
        print(num1)
        print(num2)
        return
    max_num, min_num = max(num1, num2), min(num1, num2)
    answer = [0] * 2
    for number in range(1, int(max_num * 0.5) + 1):
        if (min_num % number == 0) and (max_num % number == 0):
            answer[0] = number
    counter = 1
    while (max_num * counter) % min_num:
        counter += 1
    answer[1] = max_num * counter

    print(answer[0])
    print(answer[1])

v1, v2 = map(int, input().split())
solution(v1, v2)