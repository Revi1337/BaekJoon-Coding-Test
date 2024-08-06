import sys

input = sys.stdin.readline

'''
어두운 굴다리 (https://www.acmicpc.net/problem/17266)
'''

def solution(N, M, x):
    left, right = 1, N
    answer = 1e9
    while left <= right:
        mid = (left + right) // 2
        predicate = True
        for idx in range(M):
            if x[0] - mid > 0:
                predicate = False
                break
            if x[-1] + mid < N:
                predicate = False
                break
            if x[idx - 1] + mid < x[idx] - mid:
                predicate = False
                break

        if predicate:
            answer = min(mid, answer)
            right = mid - 1
        else:
            left = mid + 1

    return answer

N = int(input())
M = int(input())
x = list(map(int, input().split()))
print(solution(N, M, x))