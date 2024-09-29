import sys

input = sys.stdin.readline

"""
로또 (https://www.acmicpc.net/problem/6603)
2024-09-29
"""

def solution(integers):
    length = integers[0]
    integers = integers[1:]

    def recursive(depth, index, lst):
        if depth == 6:
            answer.append(lst)
            return
        for idx in range(index, length):
            recursive(depth + 1, idx + 1, lst + [integers[idx]])

    answer = []
    recursive(0, 0, [])
    for ans in answer:
        print(*ans)

while True:
    integers = list(map(int, input().split()))
    if len(integers) == 1:
        break
    solution(integers)
    print()
