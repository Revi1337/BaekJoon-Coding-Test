import sys

input = sys.stdin.readline

"""
우선 이분탐색을 위해 B 를 오름차순으로 정렬한다.
A 를 순회하며, B 에 대해 투포인터를 진행한다.
"""
def solution(n, m, numbers1, numbers2):
    answer = 0
    numbers2.sort()
    for number in numbers1:
        res = -1
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers2[mid] < number:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        answer += (res + 1)

    return answer

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().split())
    numbers1 = list(map(int, input().split()))
    numbers2 = list(map(int, input().split()))
    print(solution(n, m, numbers1, numbers2))