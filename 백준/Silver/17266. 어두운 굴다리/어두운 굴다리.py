import sys

input = sys.stdin.readline

"""
가로등의 위치 X 에서 idx 1 의 위치는 따로 검사한다.
나머지는 이분탐색으로 풀면 될 것 같다.
"""
def solution(N, M, X):
    left, right, mid = 1, N, 0
    answer = float('inf')
    flag = False
    while left <= right:
        mid = (left + right) // 2
        flag = True
        if X[0] - mid > 0:
            flag = False
        elif X[M - 1] + mid < N:
            flag = False
        else:
            for idx in range(1, M - 1):
                if X[idx] + mid < X[idx + 1] - mid:
                    flag = False
                    break
        if flag:
            answer = min(mid, answer)
            right = mid - 1
        else:
            left = mid + 1

    return answer

N = int(input().rstrip())
M = int(input().rstrip())
X = list(map(int, input().split()))
print(solution(N, M, X))
