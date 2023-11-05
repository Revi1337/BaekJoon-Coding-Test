values = [int(input()) for _ in range(9)]
ma = values[0]
index = 0
for idx in range(1, len(values)):
    if values[idx] > ma:
        ma = values[idx]
        index = idx
print(ma)
print(index + 1)