import sys

input = sys.stdin.readline

def solution(n, numbers):
    sorted_numbers = sorted(numbers)
    frequency = dict()
    sum_number = 0
    for number in sorted_numbers:
        frequency[number] = frequency.get(number, 0) + 1
        sum_number += number

    # 산술평균 & 중앙값
    print(round(sum_number / n))
    print(sorted_numbers[n // 2])

    frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    most_frequency = frequency[0][1]
    fre = cnt = 0
    for number, counter in frequency:
        if counter == most_frequency:
            cnt += 1
            fre = number
        if cnt == 2:
            break

    # 최빈값
    print(fre)

    # 최대값과 최솟값의 차
    print(sorted_numbers[-1] - sorted_numbers[0])

n = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(n)]
solution(n, numbers)
