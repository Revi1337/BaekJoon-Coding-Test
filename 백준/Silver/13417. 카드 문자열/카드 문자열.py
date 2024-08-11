import sys
from collections import deque

input = sys.stdin.readline

'''
카드 문자열 (https://www.acmicpc.net/problem/13417)
'''

def solution(N, cards):
    cards = deque(list(cards))
    answer = deque([cards.popleft()])
    front = answer[0]
    while cards:
        if cards[0] > front:
            answer.append(cards.popleft())
        else:
            curr = cards.popleft()
            answer.appendleft(curr)
            front = curr

    return "".join(answer)

T = int(input())
for _ in range(T):
    N = int(input())
    cards = input().split()
    print(solution(N, cards))



