t = int(input())

res = []
for i in range(t):
    pre = list(map(int, input().split()))
    res.append(round(sum(pre) / len(pre)))

for i, v in enumerate(res):
    print("#{} {}".format(i + 1, v))    