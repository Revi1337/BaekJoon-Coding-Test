import sys

input = sys.stdin.readline

def solution(N):

    def permutations(current, length):
        if length == N:
            print(*current)
            return
        for number in range(1, N + 1):
            if number not in current:
                current.append(number)
                permutations(current, length + 1)
                current.pop()

    permutations([], 0)

N = int(input())
solution(N)
