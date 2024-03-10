import sys

input = sys.stdin.readline

def solution(n, cards, m, inventory):
    cards = sorted(cards)
    for integer in inventory:
        left, right = 0, n - 1
        exist = False
        while left <= right:
            mid = (left + right) // 2
            if cards[mid] > integer:
                right = mid - 1
            elif cards[mid] < integer:
                left = mid + 1
            else:
                exist = True
                break
        print(1 if exist else 0, end = ' ')

n = int(input())
integers = list(map(int, input().split()))
m = int(input())
inventory = set(map(int, input().split()))
solution(n, integers, m, inventory)
