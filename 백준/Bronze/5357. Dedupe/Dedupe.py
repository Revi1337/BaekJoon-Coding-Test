loop = int(input())
for _ in range(loop):
    seed = input()
    buffer = seed[0]
    print(buffer, end = "")
    for value in seed:
        if buffer == value:
            continue
        buffer = value
        print(buffer, end = "")
    print()

