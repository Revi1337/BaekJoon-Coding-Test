import sys

input = sys.stdin.readline

def solution(N, words):
    answer = 0
    for idx in range(N):
        stack = []
        for val in words[idx]:
            if not stack:
                stack.append(val)
            elif stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)
        if not stack:
            answer += 1
    return answer

N = int(input())
words = [input().rstrip() for _ in range(N)]
print(solution(N, words))
