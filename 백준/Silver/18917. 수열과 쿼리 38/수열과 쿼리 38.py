import sys

input = sys.stdin.readline

def solution(M, queries):
    dat = {0: [0]}
    idx = 1
    sumN = 0
    xor = 0
    for query in queries:
        if query[0] == 1:
            if query[1] not in dat:
                dat[query[1]] = [idx]
            else:
                dat[query[1]].append(idx)
            sumN += query[1]
            xor ^= query[1]
            idx += 1
        elif query[0] == 2:
            dat[query[1]].pop() # 맨 앞껄 지우라고하지만 순서가 중요하지 않음.
            sumN -= query[1]
            xor ^= query[1]
        elif query[0] == 3:
            print(sumN)
        else:
            print(xor)

M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]
solution(M, queries)