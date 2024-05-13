def solution(N):
    book = {'3', '6', '9'}
    for integer in range(1, N + 1):
        counter = 0
        for char in str(integer):
            if char in book:
                counter += 1
        if not counter:
            print(integer, end = ' ')
        else:
            print('-' * counter, end = ' ')

N = int(input())
solution(N)
