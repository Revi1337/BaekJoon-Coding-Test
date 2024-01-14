def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    sum = 1 + n
    for integer in range(2, n // 2 + 1):
        if not n % integer:
            sum += integer 
    return sum
        