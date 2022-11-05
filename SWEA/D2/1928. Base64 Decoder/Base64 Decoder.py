mappedlst = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
for cnt, v in enumerate(range(int(input()))):
    val = list(input())
    res = ""
    for i, k in enumerate(val):
        val[i] = bin(mappedlst.index(k)).replace('0b', '').zfill(6)
        res += val[i]
    length = 8
    val = ""
    for i in range(0, len(res), length):
        val += chr(int(str(res[i : i + 8]), 2))
    print("#{} {}".format(cnt + 1, val))