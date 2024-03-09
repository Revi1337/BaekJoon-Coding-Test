import sys

input = sys.stdin.readline

def solution(k, n, datas):
    max_cable = max(datas)
    left, right = 1, max_cable
    answer = 0

    def count(length):
        cnt = 0
        for x in datas:
            cnt += (x // length)
        return cnt

    while left <= right:
        mid = (left + right) // 2
        if count(mid) >= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

k, n = map(int, input().split())
datas = [int(input().rstrip()) for _ in range(k)]
print(solution(k, n, datas))
