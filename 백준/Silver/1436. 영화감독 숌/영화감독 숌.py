import sys

input = sys.stdin.readline

"""
영화감독 숌 (https://www.acmicpc.net/problem/1436)

- 문제 자체를 이해하지 못했음.. 물론 내가 못하는거겠지만 말을 이렇게 좆같이 해놀 필요가 있었나 싶다.
"""

def solution(integer):
    first = 666  # 처음 666인 수
    while integer != 0:  # integer 이 0이 아니면 계속 반복
        if '666' in str(first):  # 만약 666이란 문자열이 문자열(first)안에 있으면
            integer = integer - 1  # integer을 1 감소시키고
            if integer == 0:  # 만약 integer 이 0이면
                break  # 반복문을 탈출한다.
        first = first + 1  # first의 값을 1 증가시킨다.
    return first

print(solution(int(input().rstrip())))