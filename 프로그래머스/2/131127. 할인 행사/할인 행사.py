def solution(want, number, discount):
    counter = {}
    for idx in range(len(want)):
        counter[want[idx]] = number[idx]

    ans = 0
    for idx in range(len(discount) - 10 + 1):
        cache = {**counter}
        for jdx in range(idx, idx + 10):
            if discount[jdx] in cache and cache[discount[jdx]]:
                cache[discount[jdx]] -= 1
        if not sum(cache.values()):
            ans += 1

    return ans