def solution(N, numbers):
    numbers.sort()

    while numbers:
        num = numbers.pop()
        length = len(numbers)
        for idx in range(length):
            left, right = idx, length - 1
            while left <= right:
                sm = numbers[idx] + numbers[left] + numbers[right]
                if sm == num:
                    return num
                if sm > num:
                    right -= 1
                else:
                    left += 1

N = int(input())
numbers = [int(input()) for _ in range(N)]
print(solution(N, numbers))