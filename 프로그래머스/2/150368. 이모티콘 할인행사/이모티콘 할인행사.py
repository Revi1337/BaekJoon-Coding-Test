def solution(users, emoticons):

    def recursive(lst):
        if len(lst) == len(emoticons):
            dises.append([*lst])
            return
        for dis in 10, 20, 30, 40:
            lst.append(dis)
            recursive(lst)
            lst.pop()

    dises = []
    recursive([])

    candi = []
    for discounts in dises:
        tmp = [0, 0]
        for udis, ulim in users:
            sm = 0
            for iidx, idis in enumerate(discounts):
                if idis >= udis:
                    sm += int(((100 - idis) * 0.01) * emoticons[iidx])
                    if sm >= ulim:
                        tmp[0] += 1
                        break
            else:
                tmp[1] += sm
        if sum(tmp) != 0:
            candi.append(tmp)

    candi.sort(key=lambda x: (-x[0], -x[1]))
    return candi[0]