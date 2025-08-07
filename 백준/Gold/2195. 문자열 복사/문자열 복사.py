import sys

input = sys.stdin.readline

def solution(S, P):
    slen, plen, ans = len(S), len(P), 0
    sidx = 0
    while sidx < plen:
        idxes = [idx for idx in range(slen) if S[idx] == P[sidx]]
        mxs = []
        for pidx in idxes:
            cnt = 0
            for nidx in range(sidx, plen):
                if pidx + nidx - sidx >= slen:
                    break
                if P[nidx] == S[pidx + nidx - sidx]:
                    cnt += 1
                else:
                    break
            if cnt:
                mxs.append(cnt)
        sidx += max(mxs)
        ans += 1

    return ans

S = input().rstrip()
P = input().rstrip()
print(solution(S, P))
