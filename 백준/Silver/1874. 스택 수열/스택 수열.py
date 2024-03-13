import sys

input = sys.stdin.readline

def solution(n, numbers):
    stack = []
    answer = []
    flag = 0
    offset = 1
    for number in numbers:
        while offset <= number:
            stack.append(offset)
            answer.append('+')
            offset += 1
        if stack[-1] == number:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            flag = 1
            break
    if flag == 0:
        for ans in answer:
            print(ans)

n = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(n)]
solution(n, numbers)


