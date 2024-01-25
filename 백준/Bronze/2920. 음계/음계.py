def solution(number):
    if number == sorted(number):
        print('ascending')
    elif number == sorted(number, reverse=True):
        print('descending')
    else:
        print('mixed')

solution(list(map(int, input().split())))

