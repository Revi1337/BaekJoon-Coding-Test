import sys
from itertools import combinations_with_replacement as combinations

open = sys.stdin.readline

def solution(N):
    book = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    answer = set()
    comb = combinations(book, N)
    for line in comb:
        tmp = 0
        for char in line:
            tmp += book[char]
        answer.add(tmp)
    return len(answer)

N = int(input())
print(solution(N))