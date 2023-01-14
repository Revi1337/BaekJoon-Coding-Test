t = int(input())
for _ in range(t):
	i, v = input().split()
	for x in v:
		print(x * int(i), end='')
	print()
