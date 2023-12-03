def solution(num):
    if num == 1:
        print('')
        return
    for val in range(2, num + 1):   # 2부터 하나씩 나눈다.
        if num % val == 0:          # 나머지가 0 이면
            while num % val == 0:   # 해당 숫자로 나눌 수 없을 때까지 나눈다.
                print(val)
                num /= val

solution(int(input()))
