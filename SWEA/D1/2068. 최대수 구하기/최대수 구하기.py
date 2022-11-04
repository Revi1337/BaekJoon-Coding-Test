res = []
for _ in range(int(input())):
    res.append(max(map(int, input().split())))

for i, v in enumerate(res):
    print("#{} {}".format(i + 1, v))