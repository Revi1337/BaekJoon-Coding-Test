import sys

input = sys.stdin.readline

def solution(n, m, monsters, questions):
    monsters = ['0'] + monsters
    monsters_dict = {name: idx for idx, name in enumerate(monsters)}
    for question in questions:
        if question in monsters_dict:
            print(monsters_dict[question])
        else:
            print(monsters[int(question)])

n, m = map(int, input().split())
monsters = [input().strip() for _ in range(n)]
questions = [input().strip() for _ in range(m)]
solution(n, m, monsters, questions)