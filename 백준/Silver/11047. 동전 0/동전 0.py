n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

result = 0
for i in range(n-1, -1, -1):
	if coin[i] <= k:
		tmp = k // coin[i]
		result += tmp
		k -= tmp * coin[i]
print(result)
