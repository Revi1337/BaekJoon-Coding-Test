import sys

input = sys.stdin.readline

def solution(K, arr):

    def recursive(d, arr):
        if not len(arr):
            return

        mid = len(arr) // 2
        ans[d].append(arr[mid])

        left, right = arr[:mid], arr[mid + 1:]
        recursive(d + 1, left)
        recursive(d + 1, right)

    ans = [[] for _ in range(K)]
    recursive(0, arr)

    for lst in ans:
        print(*lst, sep = ' ')

K = int(input())
arr = list(map(int, input().split()))
solution(K, arr)


