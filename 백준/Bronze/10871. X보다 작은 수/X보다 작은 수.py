_, x = map(int, input().split())
datas = list(map(int, input().split()))
answer = []
for data in datas:
    if data < x:
        answer.append(str(data))
print(" ".join(answer))
