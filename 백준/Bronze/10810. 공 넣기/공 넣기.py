n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        basket[idx - 1] = k
print(*basket)


