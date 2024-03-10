import sys

input = sys.stdin.readline

def solution(n, datas, max_price):
    max_num = max(datas)
    left, right = 1, max_num

    def counter(mid):
        counter = 0
        for price in datas:
            counter += min(price, mid)
        return counter

    while left <= right:
        mid = (left + right) // 2
        cnt = counter(mid)
        if cnt == max_price:
            return mid
        if cnt < max_price:
            left = mid + 1
        else:
            right = mid - 1

    return right

n = int(input())
datas = list(map(int, input().split()))
max_price = int(input())
print(solution(n, datas, max_price))
