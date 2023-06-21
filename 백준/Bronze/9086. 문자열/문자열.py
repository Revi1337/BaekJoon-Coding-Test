loop = int(input())
for _ in range(loop):
    seed = input()
    if len(seed) == 1:
        print(seed*2)
    else:
        print(seed[0] + seed[-1])