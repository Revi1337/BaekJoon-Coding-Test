import sys

input = sys.stdin.readline

def solution(s):
    total = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            total.add(s[i:j + 1])
    return len(total)

s = input().rstrip()
print(solution(s))
