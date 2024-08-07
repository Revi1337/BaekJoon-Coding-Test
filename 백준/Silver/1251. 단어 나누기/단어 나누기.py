import sys

input = sys.stdin.readline

'''
단어 나누기 (https://www.acmicpc.net/problem/1251)
'''

def solution(word):
    length = len(word)
    words = []
    for i in range(length):
        for j in range(i, length):
            prefix = word[:i]
            middle = word[i:j]
            postfix = word[j:]
            if prefix != '' and middle != '' and postfix != '':
                words.append(prefix[::-1] + middle[::-1] + postfix[::-1])

    return sorted(words)[0]

word = input().rstrip()
print(solution(word))

