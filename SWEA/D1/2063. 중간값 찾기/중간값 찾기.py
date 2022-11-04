n = int(input())

res = sorted(list(map(int, input().split())))
print(res[len(res) // 2])