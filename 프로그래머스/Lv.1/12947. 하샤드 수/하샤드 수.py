def solution(x):
    number = sum(map(int, str(x)))
    print(number)
    return True if x % number == 0 else False
