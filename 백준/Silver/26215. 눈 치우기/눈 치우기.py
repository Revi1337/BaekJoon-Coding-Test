import sys

input = sys.stdin.readline

def solution(N, snows):
    sdict = dict(enumerate(snows))
    timer = 0
    while sdict:
        skey = sorted(sdict, key=lambda k: -sdict[k])
        counter = 0
        clst = []
        for k in skey:
            if sdict[k] >= 1:
                counter += 1
                clst.append(k)
                if counter >= 2:
                    break

        if counter == 1:
            k = clst[0]
            sdict[k] -= 1
            if sdict[k] == 0:
                sdict.pop(k)
                skey.remove(k)
        elif counter == 2:
            for k in clst[:2]:
                sdict[k] -= 1
                if sdict[k] == 0:
                    sdict.pop(k)
                    skey.remove(k)

        if counter != 0:
            timer += 1
        if timer > 1440:
            return -1

    return timer

N = int(input())
snows = list(map(int, input().split()))
print(solution(N, snows))