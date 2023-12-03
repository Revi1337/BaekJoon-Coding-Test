def solution(num):
    if num == 1:
        print('')
        return
    for val in range(2, num + 1):
        if num % val == 0:
            while num % val == 0:
                print(val)
                num /= val

solution(int(input()))