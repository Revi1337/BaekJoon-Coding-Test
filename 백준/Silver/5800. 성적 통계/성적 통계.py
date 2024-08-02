import sys

input = sys.stdin.readline

def solution(n, datas):
    lst = []
    for data in datas:
        d = sorted(data[1:], reverse=True)
        pre = [f'Max {max(d)}', f'Min {min(d)}']
        minN = -1e9
        for idx in range(len(d) - 1):
            minN = max(minN, d[idx] - d[idx + 1])
        pre.append(f'Largest gap {minN}')
        lst.append(pre)

    for idx, val in enumerate(lst, start=1):
        print(f'Class {idx}')
        print(*val, sep=', ')

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
solution(n, datas)
