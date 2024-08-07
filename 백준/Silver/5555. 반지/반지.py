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
        for start in range(length):
            end = (start + tlength) % length
            if end > start:
                string = ring[start : end]
            else:
                string = ring[start:] + ring[:end]
            if string == t:
                answer += 1
                break
    return answer

t = input().rstrip()
N = int(input())
rings = [input().rstrip() for _ in range(N)]
print(solution(t, N, rings))

