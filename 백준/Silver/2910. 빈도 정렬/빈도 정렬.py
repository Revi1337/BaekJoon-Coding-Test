import sys

input = sys.stdin.readline

'''
빈도 정렬 (https://www.acmicpc.net/problem/2910)
'''

def solution(N, C, mes):
    freq = {}
    for idx, val in enumerate(mes):
        freq[val] = freq.get(val, [0, idx])
        freq[val][0] += 1
    items = list(freq.items())
    items.sort(key = lambda x: (-x[1][0], x[1][1]))

    answer = []
    for key, (counter, _) in items:
        answer.append(((str(key) + ' ') * counter)[:-1])

    print(*answer, sep = ' ')

N, C = map(int, input().split())
mes = list(map(int, input().split()))
solution(N, C, mes)