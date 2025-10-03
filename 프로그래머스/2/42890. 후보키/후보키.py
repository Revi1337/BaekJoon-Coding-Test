from itertools import combinations

def solution(relation):

    idxes = list(range(len(relation[0])))
    keys = set()
    for size in range(1, len(relation[0]) + 1):
        for comb in list(combinations(idxes, size)):
            counter = set()
            for row in relation:
                tup = tuple(row[idx] for idx in comb)
                counter.add(tup)
            if len(counter) == len(relation):
                s = set(idx for idx in comb)
                for k in keys:
                    k = set(k)
                    if k.issubset(s):
                        break
                else:
                    keys.add(tuple(s))

    return len(keys)