n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for r in range(j + 1, n):
            value = numbers[i] + numbers[j] + numbers[r]
            if value <= m:
                answer.append(value)
print(max(answer))
