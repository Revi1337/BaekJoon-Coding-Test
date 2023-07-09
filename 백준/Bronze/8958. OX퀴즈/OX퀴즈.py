loop = int(input())
for _ in range(1, loop + 1):
    seed = input()
    sum = 0
    score = 0
    for val in seed:
        if val == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)