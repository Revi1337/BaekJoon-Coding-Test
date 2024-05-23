import sys

open = sys.stdin.readline

def solution(N):

    def get_clock(string):
        min_str = int(string)
        for _ in range(4):
            string = string[1:] + string[0]
            min_str = min(min_str, int(string))
        return min_str

    init = get_clock("".join(map(str, N)))
    book = [0] * 10000
    book[1111] = 1
    prev = 1111
    for number in range(1112, 10000):
        clock = get_clock(str(number))
        if book[clock] == 0 and '0' not in str(number):
            book[number] = book[prev] + 1
            prev = number
    return book[int(init)]

N = list(map(int, input().split()))
print(solution(N))
