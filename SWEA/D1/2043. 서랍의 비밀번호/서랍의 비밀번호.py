p, k = map(int, input().split())

print(p - k + 1) if p > k else print(abs(p - k) + 1)
