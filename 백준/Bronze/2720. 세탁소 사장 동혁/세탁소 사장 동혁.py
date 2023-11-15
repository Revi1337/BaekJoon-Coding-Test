def solution(left):
    coin = {'25': 0, '10': 0, '5': 0, '1': 0}
    cnt = 0
    for tp in coin:
        if (left // int(tp)) != 0:
            coin[tp] += left // int(tp)
            cnt += left // int(tp)
            left = left % int(tp)
    return " ".join(map(str, coin.values()))

t = int(input())
for _ in range(t):
    print(solution(int(input())))