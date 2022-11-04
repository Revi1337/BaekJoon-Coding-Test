for i in range(5)[::-1]:
    for v in range(5)[::-1]:
        if i == v:
            print("#", end = "")
        else:
            print("+", end = "")
    print()