n, b = input().split()
n = ''.join(reversed(n))
b = int(b)
data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = 0
for idx in range(len(n) - 1, -1, -1):
    answer += data.index(n[idx]) * (b ** idx)
print(answer)
