def solution(price, money, count):
    sum = 0
    for cnt in range(1, count + 1):
        sum += price * cnt
    return sum - money if sum > money else 0