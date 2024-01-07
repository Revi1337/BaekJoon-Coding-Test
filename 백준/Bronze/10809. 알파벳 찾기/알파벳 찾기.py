import sys

def solution(data):
    answer = [-1] * 26
    for idx in range(len(data)):
        if answer[ord(data[idx]) - 97] == -1:
            answer[ord(data[idx]) - 97] = idx
    for char in answer:
        print(char, end = ' ')

data = sys.stdin.readline().rstrip()
solution(data)
