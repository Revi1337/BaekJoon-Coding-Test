import sys

input = sys.stdin.readline

def solution(N, classes, M, empties):
    sdict = {}
    for idx, empty in enumerate(empties):
        edict = {i: set() for i in range(0, 5)}
        for e in empty:
            day, clazz = e // 10, e % 10
            if clazz == 0:
                day -= 1
            edict[day].add(clazz)
        sdict[idx] = edict

    dat = [0] * M
    for stu in sdict:
        for idx, clazz in enumerate(classes):
            poss = True
            for c in clazz:
                day, time = c // 10, c % 10
                if time == 0:
                    day -= 1
                if time not in sdict[stu][day]:
                    poss = False
                    break
            if poss:
                dat[stu] += 1

    for d in dat:
        print(d)


N = int(input())
classes = [list(map(int, input().split()))[1:] for _ in range(N)]
M = int(input())
empties = [list(map(int, input().split()))[1:] for _ in range(M)]
solution(N, classes, M, empties)