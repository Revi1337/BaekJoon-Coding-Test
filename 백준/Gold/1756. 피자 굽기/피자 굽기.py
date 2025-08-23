import sys

input = sys.stdin.readline

def solution(D, N, arr, t):
    marr = [0] * D
    marr[0] = arr[0]
    for idx in range(1, D):
        marr[idx] = min(marr[idx - 1], arr[idx])

    pos = D - 1
    for val in t:
        tmp, left, right = -1, 0, pos
        while left <= right:
            mid = (left + right) // 2
            if marr[mid] >= val:
                tmp = mid
                left = mid + 1
            else:
                right = mid - 1
        if tmp == -1:
            return 0
        pos = tmp - 1

    return tmp + 1

D, N = map(int, input().split())
arr = list(map(int, input().split()))
t = list(map(int, input().split()))
print(solution(D, N, arr, t))