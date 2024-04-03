import sys

input = sys.stdin.readline

def solution(n, note1, m, note2):
    book = set(note1)
    for number in note2:
        if number in book:
            print(1)
        else:
            print(0)

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    note1 = list(map(int, input().split()))
    m = int(input().rstrip())
    note2 = list(map(int, input().split()))
    solution(n, note1, m, note2)