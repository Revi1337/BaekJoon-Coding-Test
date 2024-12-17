import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

n = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))

answer = defaultdict(set)
visited = set()

for i in range(n):
    answer[P[i]].add(i)

cnt = 0
cards = list(range(n))
while True:
    first,second,third = set(cards[0:n:3]), set(cards[1:n:3]), set(cards[2:n:3])
    if first == answer[0] and second == answer[1] and third == answer[2]:
        break
    if tuple(cards) in visited:
        cnt = -1
        break
    visited.add(tuple(cards))
    temp = [0] * n
    for i in range(n):
        temp[S[i]] = cards[i]
    cards = temp
    cnt += 1
print(cnt)