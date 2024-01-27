n = int(input())
datas = set(input().split())
m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    if str(target) in datas:
        print(1)
    else:
        print(0)