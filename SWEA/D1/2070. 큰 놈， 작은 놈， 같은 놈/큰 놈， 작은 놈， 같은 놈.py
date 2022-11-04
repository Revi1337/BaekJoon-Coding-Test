res = []
for i in range(int(input())):
    res.append(list(map(int, input().split())))

for i, v in enumerate(res):
    if v[0] == v[-1]: operator = "="
    elif v[0] < v[-1]: operator = "<"
    elif v[0] > v[-1]: operator = ">"
    print("#{} {}".format(i + 1, operator))