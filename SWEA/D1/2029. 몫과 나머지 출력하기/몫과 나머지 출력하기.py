res = [list(map(int, input().split())) for _ in range(int(input()))]

for i, v in enumerate(res):
    val = divmod(v[0], v[-1])
    print("#{} {} {}".format(i + 1, val[0], val[1]))
