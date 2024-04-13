import sys

input = sys.stdin.readline

def solution(n, m, entries, questions):
    entries = {site: password for (site, password) in entries}
    for question in questions:
        print(entries[question])

n, m = map(int, input().split())
entries = [input().rstrip().split(' ') for _ in range(n)]
questions = [input().rstrip() for _ in range(m)]
solution(n, m, entries, questions)