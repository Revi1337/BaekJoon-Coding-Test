n = int(input())
scores = list(map(int, input().split()))
max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
sum = 0
for score in scores:
    sum += score / max_score * 100
print(sum / n)