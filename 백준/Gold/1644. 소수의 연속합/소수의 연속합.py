import sys

input = sys.stdin.readline

def solution(n):
    # 에라토스테네스체 알고리즘으로 (소수배열을 구한 후)
    if n == 1:
        return 0
    arr = [1] * (n + 1)
    numbers = []
    for number in range(2, int(n ** 0.5) + 1):
        if arr[number]:
            offset = 2
            while number * offset <= n:
                arr[number * offset] = 0
                offset += 1
    for number in range(2, n + 1):
        if arr[number]:
            numbers.append(number)


    # Two Pointer 알고리즘으로 소수배열의 구간합을 구하여, n 이 만들어지나 판단한다.
    counter = 0
    numbers_length = len(numbers)
    left, right = numbers_length - 1, numbers_length - 1
    cur = numbers[-1]
    while 0 <= left <= right and 0 <= right < numbers_length:
        if cur > n:
            cur -= numbers[right]
            right -= 1
        else:
            if cur == n:
                counter += 1
            left -= 1
            if left < 0:
                break
            cur += numbers[left]
    return counter

n = int(input().rstrip())
print(solution(n))
