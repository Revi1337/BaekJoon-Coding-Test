import sys

input = sys.stdin.readline

def solution(N):
    book = [0] * 10
    for num in N:
        book[int(num)] += 1

    if book[6] > book[9]:
        while abs(book[6] - book[9]) > 1:
            book[6] -= 1
            book[9] += 1
    elif book[6] < book[9]:
        while abs(book[9] - book[6]) > 1:
            book[9] -= 1
            book[6] += 1

    answer = 0
    while sum(book) > 0:
        answer += 1
        for idx in range(10):
            if book[idx] != 0:
                book[idx] -= 1

    return answer

N = input().rstrip()
print(solution(N))
