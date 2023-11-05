def solution(datas):
    sum = 0
    for data in datas:
        sum += data[0] * data[1]
    if sum != price:
        return 'No'
    return 'Yes'

price = int(input())
loop = int(input())
datas = [list(map(int, input().split())) for _ in range(loop)]
print(solution(datas))

