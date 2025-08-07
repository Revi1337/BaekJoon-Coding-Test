import sys

input = sys.stdin.readline

def solution(S):

    def possible(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True

    for s in S:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                if possible(left + 1, right) or possible(left, right - 1):
                    print(1)
                    break
                print(2)
                break
        else:
            print(0)

T = int(input())
S = [input().rstrip() for _ in range(T)]
solution(S)