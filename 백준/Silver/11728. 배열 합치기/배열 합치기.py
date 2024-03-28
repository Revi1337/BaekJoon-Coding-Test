import sys

input = sys.stdin.readline

def solution(a, b, arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    print(*arr1)

a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
solution(a, b, arr1, arr2)
