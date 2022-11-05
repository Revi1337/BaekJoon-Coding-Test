res = []
while True:
    val = input().split()
    if " ".join(val) == "# 0 0":
        break
    elif int(val[1]) > 17 or int(val[2]) >=80:
        res.append([val[0], "Senior"])
    else:
        res.append([val[0], "Junior"])

for i in res:
    for v in i:
        print(v, end = " ")
    print()