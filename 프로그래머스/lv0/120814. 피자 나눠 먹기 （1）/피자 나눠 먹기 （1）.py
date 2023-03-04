def solution(n):
    pizza = 0
    if n <= 7:
        return 1
    elif n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1

#     1  1판
#     7  2판
#     8  2판
#     9  2판
#     10 2판
#     11 2판
#     12 2판
#     13 2판
#     14 3판
#     15 3판
    
    
    