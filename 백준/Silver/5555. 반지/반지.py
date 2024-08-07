import sys

input = sys.stdin.readline

'''
반지 (https://www.acmicpc.net/problem/5555)
'''

def solution(t, N, rings):
    answer = 0
    tlength = len(t)
    for ring in rings:
        length = len(ring)
        ring *= 2
        for start in range(length):
            string = ring[start : start + tlength]
            if string == t:
                answer += 1
                break

    return answer

t = input().rstrip()
N = int(input())
rings = [input().rstrip() for _ in range(N)]
print(solution(t, N, rings))

