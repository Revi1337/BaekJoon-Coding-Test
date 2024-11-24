def solution(N, prices):
    max_price = answer = 0
    for price in prices[::-1]:
        if price > max_price:
            max_price = price
        else:
            answer += max_price - price

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, prices)}')