import sys

input = sys.stdin.readline

def solution(N, S, W, G, K, A, I, D):
    ST, MU, GI, TR = 0, N - 1, 2 * N - 2, 3 * N - 3
    gmon, kidx, kset = 0, 0, set()
    cmon, curr, purchase = S, 0, set()
    island, lim = False, 0
    jumped = False
    invoked_by_golden_key = False
    D = D[::-1]

    arr = [-1] * ((4 * N) - 4)
    cidx = 1
    for entry in A:
        if cidx in {ST, MU, GI, TR}:
            cidx += 1
        if entry[0] == 'L':
            arr[cidx] = int(entry[1])
        else:
            arr[cidx] = 0
            kset.add(cidx)
        cidx += 1

    while D:
        if island:
            for _ in range(lim):
                if not D or (D[-1][0] != D[-1][1]):
                    if D:
                        D.pop()
                else:
                    D.pop()
                    island = False
                    lim = 0
                    break
            else:
                island = False
            continue

        if jumped:
            old_curr = curr
            curr = ST
            if old_curr != ST:
                cmon += W
            jumped = False
            continue

        if not invoked_by_golden_key:
            if not D:
                break
            move = sum(D.pop())
            if curr + move >= (4 * N - 4):
                cmon += W * ((curr + move) // (4 * N - 4))
            nxt = (curr + move) % ((4 * N) - 4)
        else:
            nxt = curr
            invoked_by_golden_key = False

        if nxt == TR:
            jumped = True
            curr = nxt
            continue
        if nxt == MU:
            island = True
            lim = 3
            curr = nxt
            continue
        if nxt == ST:
            cmon += W
            curr = nxt
            continue
        if nxt == GI:
            cmon += gmon
            gmon = 0
            curr = nxt
            continue

        if nxt in kset:
            oper, x = K[kidx]
            kidx = (kidx + 1) % len(K)
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
                gmon += x
            else:
                old_nxt = nxt
                nxt = (nxt + x) % ((4 * N) - 4)
                if old_nxt + x >= (4 * N - 4):
                    cmon += W
                invoked_by_golden_key = True
                curr = nxt
                continue
            curr = nxt
        else:
            if 0 < arr[nxt] <= cmon and nxt not in purchase:
                purchase.add(nxt)
                cmon -= arr[nxt]
            curr = nxt

    return 'WIN' if len(purchase) == len(arr) - len(kset) - 4 else 'LOSE'

N, S, W, G = map(int, input().split())
K = [list(map(int, input().rstrip().split())) for _ in range(G)]
A = [input().rstrip().split() for _ in range(4 * N - 8)]
I = int(input())
D = [list(map(int, input().rstrip().split())) for _ in range(I)]
print(solution(N, S, W, G, K, A, I, D))