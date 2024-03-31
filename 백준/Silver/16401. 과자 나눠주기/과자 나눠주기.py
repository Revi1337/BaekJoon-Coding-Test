import sys

input = sys.stdin.readline

def solution(m, n, snacks):
    max_num = max(snacks)
    answer = 0
    left, right = 1, max_num
    while left <= right:
        mid = (left + right) // 2
        counter = 0
        if mid == 0:
            return 0
        for snack in snacks:
            if snack >= mid:
                counter += (snack // mid)
        if counter >= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer



m, n = map(int, input().split())
snacks = list(map(int, input().split()))
print(solution(m, n, snacks))