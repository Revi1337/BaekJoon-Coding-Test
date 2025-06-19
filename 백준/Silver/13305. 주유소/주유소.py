def solution(N, distance, price):
    sm, mn = 0, price[0]
    for idx in range(N - 1):
        sm += mn * distance[idx]
        if price[idx + 1] < mn:
            mn = price[idx + 1]

    return sm

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
print(solution(N, distance, price))