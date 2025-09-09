import sys

input = sys.stdin.readline

def solution(N, arr, M, T):
    arr.sort()
    for num in T:
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == num:
                print(1)
                break
            if arr[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        else:
            print(0)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
solution(N, arr, M, T)