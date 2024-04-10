import sys

input = sys.stdin.readline

def upper_bound(data_list, x):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return len(data_list) - (right + 1)


def solution(n, h, datas):
    rock1 = []
    rock2 = []
    for idx in range(n):
        if idx % 2 == 0:
            rock1.append(datas[idx])
        else:
            rock2.append(datas[idx])

    rock1.sort()
    rock2.sort()

    answer = n
    count = 0
    for height in range(1, h + 1):
        down_num = upper_bound(rock1, height - 1)
        up_num = upper_bound(rock2, h - height)
        total = down_num + up_num
        if total < answer:
            answer = total
            count = 1
        elif total == answer:
            count += 1

    return " ".join(map(str, [answer, count]))

n, h = map(int, input().split())
datas = [int(input().rstrip()) for _ in range(n)]
print(solution(n, h, datas))
