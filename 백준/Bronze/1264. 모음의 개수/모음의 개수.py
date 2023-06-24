while True:
    res = 0
    seed = input()
    if seed[0] == '#':
        break
    for value in seed:
        if value in list('aeiouAEIOU'):
            res += 1
    print(res)