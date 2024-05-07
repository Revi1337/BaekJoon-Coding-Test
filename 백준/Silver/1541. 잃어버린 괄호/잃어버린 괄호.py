import sys

input = sys.stdin.readline

"""
1. 연속해서 두개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
2. 수는 0 으로 시작할 수 있다.
3, 식의 길이는 50보다 작거나 같다.
"""
def solution(n):
    answer = 0
    sik = n.split('-') # 55, 50+40
    sumN = sum(map(int, sik[0].split('+')))
    if n[0] == '-':
        answer += -sumN
    else:
        answer += sumN
    for s in sik[1:]:
        answer += -sum(map(int, s.split('+')))

    return answer

n = input().rstrip()
print(solution(n))
