import sys

input = sys.stdin.readline

'''
행복한지 슬픈지 (https://www.acmicpc.net/problem/10769)
'''

def solution(string):
    emotion = [0, 0]
    for idx in range(len(string)):
        if string[idx : idx + 3] == ':-)':
            emotion[0] += 1
        elif string[idx : idx + 3] == ':-(':
            emotion[1] += 1
    if not sum(emotion):
        return 'none'
    if emotion[0] == emotion[1]:
        return 'unsure'
    if emotion[0] > emotion[1]:
        return 'happy'
    if emotion[0] < emotion[1]:
        return 'sad'

string = input().strip()
print(solution(string))