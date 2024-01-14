from math import sqrt

def solution(n):
    number = sqrt(n)
    if number.is_integer():
        return (int(number) + 1) ** 2
    return -1