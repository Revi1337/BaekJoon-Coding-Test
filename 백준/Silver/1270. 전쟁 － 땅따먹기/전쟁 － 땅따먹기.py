import sys

input = sys.stdin.readline

def solution(N, arr):
    totals, ans = [[0] * N for _ in range(2)]
    for idx, lst in enumerate(arr):
        totals[idx] = lst[0]
        freq = {}
        for num in lst[1:]:
            freq[num] = freq.get(num, 0) + 1
        ans[idx] = freq

    for idx in range(N):
        for key in ans[idx]:
            if ans[idx][key] > (totals[idx] // 2):
                print(key)
                break
        else:
            print('SYJKGW')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
solution(N, arr)

