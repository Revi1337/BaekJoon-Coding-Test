import sys

input = sys.stdin.readline

'''
누울 자리를 찾아라 (https://www.acmicpc.net/problem/1652) 
'''

def solution(N, rooms):
    answer = [0, 0]
    for row in range(N):
        counter = 0
        for col in range(N):
            if rooms[row][col] != 'X':
                counter += 1
            else:
                if counter >= 2:
                    answer[0] += 1
                counter = 0
        if counter >= 2:
            answer[0] += 1

    for col in range(N):
        ver = [row[col] for row in rooms]
        counter = 0
        for val in ver:
            if val != 'X':
                counter += 1
            else:
                if counter >= 2:
                    answer[1] += 1
                counter = 0
        if counter >= 2:
            answer[1] += 1

    return f'{answer[0]} {answer[1]}'


N = int(input())
rooms = [list(input().rstrip()) for _ in range(N)]
print(solution(N, rooms))
