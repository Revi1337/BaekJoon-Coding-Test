import sys

sys.setrecursionlimit(10 ** 6)

def solution(k, num, links):

    nlen = len(num)

    def find_root():
        counter = [0] * nlen
        for idx, (v1, v2) in enumerate(links):
            counter[idx] += 1
            if v1 != -1:
                counter[v1] += 1
            if v2 != -1:
                counter[v2] += 1
        return counter.index(min(counter))

    def count_cut(n, limit):
        if n == -1:
            return 0, 0

        lsm, lcut = count_cut(links[n][0], limit)
        rsm, rcut = count_cut(links[n][1], limit)
        if lsm + rsm + num[n] <= limit:
            return lsm + rsm + num[n], lcut + rcut
        elif min(lsm, rsm) + num[n] <= limit:
            return min(lsm, rsm) + num[n], lcut + rcut + 1
        else:
            return num[n], lcut + rcut + 2

    root = find_root()
    left, right = max(num), sum(num)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        _, cuts = count_cut(root, mid)
        if cuts < k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans