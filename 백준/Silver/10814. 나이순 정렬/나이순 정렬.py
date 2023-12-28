def solution(datas: list) -> list:
    datas.sort(key=lambda x: x[0])
    for data in datas:
        print(data[0], data[1])

loop = int(input())
datas = []
for _ in range(loop):
    data = input().split()
    datas.append([int(data[0]), data[1]])
solution(datas)