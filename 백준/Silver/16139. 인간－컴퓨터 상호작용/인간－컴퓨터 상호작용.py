def solution(S, Q, opers):
    dat = [0] * (len(S) + 1)
    dat[0] = [0] * 26
    for idx in range(len(S)):
        tmp = [*dat[idx]]
        tmp[ord(S[idx]) - 97] += 1
        dat[idx + 1] = tmp

    for char, v1, v2 in opers:
        v1, v2 = int(v1), int(v2) + 1
        print(dat[v2][ord(char) - 97] - dat[v1][ord(char) - 97])

S = input().rstrip()
Q = int(input())
opers = [input().split() for _ in range(Q)]
solution(S, Q, opers)