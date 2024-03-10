import sys

input = sys.stdin.readline

def solution(n, m, forest):
    max_length = max(forest)
    left, right = 1, max_length
    answer = 0

    def counter(mid):
        counter = 0
        for tree in forest:
            if tree > mid:
                counter += (tree - mid)
        return counter

    while left < right:
        mid = (left + right) // 2
        if counter(mid) < m:
            right = mid
        else:
            answer = mid
            left = mid + 1
    return answer

n, m = map(int, input().split())
forest = list(map(int, input().split()))
print(solution(n, m, forest))
