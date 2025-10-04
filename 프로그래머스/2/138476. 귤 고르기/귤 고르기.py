def solution(k, tangerine):
    counter = {}
    for size in tangerine:
        counter[size] = counter.get(size, 0) + 1
    sdict = {key: counter[key] for key in sorted(counter.keys(), key = lambda k: -counter[k])}

    ans = 0
    for key, cnt in sdict.items():
        k -= cnt
        ans += 1
        if k <= 0:
            return ans