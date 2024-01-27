def solution(datas):
    length = len(datas)
    answer = [1] * length
    for i in range(length):
        for j in range(length):
            w1, h1 = datas[i]
            w2, h2 = datas[j]
            if w1 < w2 and h1 < h2:
                answer[i] += 1
    for idx in range(length):
        print(answer[idx], end = ' ')

loop = int(input())
datas = [tuple(map(int, input().split())) for _ in range(loop)]
solution(datas)
