res = list(input())
res = "".join([i.lower() if i.isupper() else i.upper() for i in res])
print(res)
