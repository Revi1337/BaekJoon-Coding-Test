import sys

input = sys.stdin.readline

'''
영단어 암기는 괴로워 (https://www.acmicpc.net/problem/20920)
'''

def solution(N, M, words):
    frequency = {}
    for word in words:
        wlength = len(word)
        if wlength >= M:
            frequency[word] = frequency.get(word, [0, wlength])
            frequency[word][0] += 1
            frequency[word].append(word)

    values = [*frequency.values()]
    values.sort(key = lambda x: (-x[0], -x[1], x[2]))

    for *_, answer in values:
        print(answer)

N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
solution(N, M, words)