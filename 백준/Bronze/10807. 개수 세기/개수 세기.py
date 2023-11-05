_ = int(input())
datas = list(map(int, input().split()))
find = int(input())

cnt = 0
for data in datas:
    if data == find:
        cnt += 1
print(cnt)