import sys

input = sys.stdin.readline

def solution(dad, mom):
    answer = set()
    answer.add((dad[0], dad[0]))
    answer.add((dad[1], dad[1]))
    answer.add((mom[0], mom[0]))
    answer.add((mom[1], mom[1]))

    answer.add((dad[0], dad[1]))
    answer.add((dad[1], dad[0]))
    answer.add((mom[0], mom[1]))
    answer.add((mom[1], mom[0]))

    for d in dad:
        for m in mom:
            answer.add((d, m))
            answer.add((m, d))

    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    for (v1, v2) in answer:
        print(f'{v1} {v2}')

dad = input().rstrip().split()
mom = input().rstrip().split()
solution(dad, mom)

