import sys

input = sys.stdin.readline

def solution(n, numbers, m, d):
    sorted_numbers = sorted(numbers)
    sorted_dict = {}
    for idx, value in enumerate(sorted_numbers):
        if value not in sorted_dict:
            sorted_dict[value] = idx

    for target in d:
        if target in sorted_dict:
            print(sorted_dict[target])
        else:
            print(-1)

n, m = map(int, input().split())
numbers = [int(input().rstrip()) for _ in range(n)]
d = [int(input().rstrip()) for _ in range(m)]
solution(n, numbers, m, d)
