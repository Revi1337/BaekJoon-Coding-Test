data = [0] * 42
for _ in range(10):
    left = int(input()) % 42
    data[left] += 1
ans = 0
for idx in range(len(data)):
    if data[idx] != 0:
        ans += 1
print(ans)
