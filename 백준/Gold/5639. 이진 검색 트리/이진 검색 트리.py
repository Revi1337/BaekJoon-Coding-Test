# 2026-04-25
# https://www.acmicpc.net/problem/5639
# 이진 검색 트리
# tree
# dfs (pre order -> post order 원복)

import sys

sys.setrecursionlimit(10 ** 5)

"""
(pre order) 50 30 24 5 28 45 98 52 60
 to
(post order) 5 28 24 45 30 60 52 98 50
                 
50 (30 24 5 28 45) (98 52 60)
50 (30 (24 5 28) (45)) (98 (52 60))
50 (30 (24 (5) (28)) (45)) (98 (52 (60)))

"""
def solution(arr):

    def rollback(arr):
        if not arr:
            return

        left, mid, right = [], arr[0], []
        for idx in range(1, len(arr)):
            if arr[idx] > mid:
                left, right = arr[1:idx], arr[idx:]
                break
        else:
            left = arr[1:]

        rollback(left)
        rollback(right)
        print(mid)

    rollback(arr)

arr = []
while True:
    try:
        node = int(input())
        arr.append(node)
    except:
        break
solution(arr)