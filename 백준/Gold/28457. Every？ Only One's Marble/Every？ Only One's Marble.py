import sys

input = sys.stdin.readline

def solution(N, S, W, G, GO, A, I, D):
    ST, MU, GI, SP, GOLD = -1, -10, -20, -30, -40
    arr = [0] * ((4 * N) - 4)
    arr[0], arr[N - 1], arr[2 * N - 2], arr[3 * N - 3] = ST, MU, GI, SP
    golds = set()
    cidx = 1
    for entry in A:
        if cidx in {0, N - 1, 2 * N - 2, 3 * N - 3}:
            cidx += 1
        if entry[0] == 'L':
            arr[cidx] = int(entry[1])
        else:
            arr[cidx] = GOLD
            golds.add(cidx)
        cidx += 1

    D = D[::-1]
    cmon, cidx, purchase = S, 0, set()
    gimon = gidx = island = 0
    while D:
        d1, d2 = D.pop()
        if island:
            island -= 1
            if d1 == d2:
                island = 0
            continue

        cidx += d1 + d2
        if cidx >= (N * 4) - 4:
            cmon += W * (cidx // (N * 4 - 4))
        cidx = cidx % (N * 4 - 4)

        if arr[cidx] == MU:
            island = 3
            continue
        if arr[cidx] == GI:
            cmon += gimon
            gimon = 0
            continue
        if arr[cidx] == SP:
            cidx = 0
            cmon += W
            continue
        if arr[cidx] > 0:
            if cmon >= arr[cidx] and cidx not in purchase:
                purchase.add(cidx)
                cmon -= arr[cidx]
            continue

        if arr[cidx] == GOLD:
            oper, x = GO[gidx]
            gidx = (gidx + 1) % len(GO)
            if oper == 1:
                cmon += x
            elif oper == 2:
                if cmon < x:
                    return 'LOSE'
                cmon -= x
            elif oper == 3:
                if cmon < x:
                    return 'LOSE'
                cmon -= x
                gimon += x
            else:
                cidx += x
                if cidx >= (N * 4) - 4:
                    cmon += W * (cidx // (N * 4 - 4))
                cidx = cidx % (N * 4 - 4)

                if arr[cidx] == MU:
                    island = 3
                elif arr[cidx] == GI:
                    cmon += gimon
                    gimon = 0
                elif arr[cidx] == SP:
                    cidx = 0
                    cmon += W
                elif arr[cidx] > 0:
                    if cmon >= arr[cidx] and cidx not in purchase:
                        purchase.add(cidx)
                        cmon -= arr[cidx]

    return 'WIN' if len(purchase) == len(arr) - len(golds) - 4 else 'LOSE'

N, S, W, G = map(int, input().split())
GO = [list(map(int, input().rstrip().split())) for _ in range(G)]
A = [input().rstrip().split() for _ in range(4 * N - 8)]
I = int(input())
D = [list(map(int, input().rstrip().split())) for _ in range(I)]
print(solution(N, S, W, G, GO, A, I, D))