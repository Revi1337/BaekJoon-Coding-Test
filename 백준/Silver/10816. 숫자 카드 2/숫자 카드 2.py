from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

counter = Counter(cards)
for t in target:
    cnt = counter.get(t)
    if cnt is None:
        print(0, end = ' ')
    else:
        print(cnt, end = ' ')