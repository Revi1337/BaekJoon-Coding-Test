def solution(N, info):

    def comb(lst, st):
        if len(lst) == N:
            combs.append([*lst])
            return
        for idx in range(st, 11):
            lst.append(idx)
            comb(lst, idx)
            lst.pop()

    combs = []
    comb([], 0)

    lions = []
    for hits in combs:
        score = [0] * 11
        for hit in hits:
            score[10 - hit] += 1
        lions.append(score)

    candi = []
    for lion in lions:
        diff = [0, 0]
        for idx in range(11):
            ac, lc = info[idx], lion[idx]
            if not ac and not lc:
                continue
            if ac >= lc:
                diff[0] += 10 - idx
            else:
                diff[1] += 10 - idx
        if diff[1] > diff[0]:
            candi.append([diff, lion])

    candi.sort(key=lambda x: -(x[0][1] - x[0][0]))

    return candi[0][1] if candi else [-1]