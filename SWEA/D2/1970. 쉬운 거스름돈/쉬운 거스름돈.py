def solution(idx, price):
    book = [50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10]
    answer = {}
    for won in book:
        mok = price // won
        answer[won] = answer.get(won, 0) + mok
        price -= (mok * won)
    print(f'#{idx}')
    print(*[answer[won] for won in book])

T = int(input())
for idx in range(T):
    price = int(input())
    solution(idx + 1, price)
