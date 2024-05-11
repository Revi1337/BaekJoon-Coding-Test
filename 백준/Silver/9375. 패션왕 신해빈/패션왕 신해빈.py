import sys

input = sys.stdin.readline

def solution(n, passion):
    cloths = {}
    answer = 1
    for _, value in passion:
        cloths[value] = cloths.get(value, 0) + 1
    for kind in cloths:
        answer *= (cloths[kind] + 1) # +1 은 안입는 경우의 수를 포함
    return answer - 1 # -1 은 모두 안입는 것.

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    passion = [input().rstrip().split() for _ in range(n)]
    print(solution(n, passion))
