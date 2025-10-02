def solution(numbers):

    def recursive(lst):
        nonlocal cant
        if cant:
            return

        midx = len(lst) // 2
        left, right = lst[:midx], lst[midx + 1:]
        if left:
            if lst[midx] == '0' and '1' in left:
                cant = True
                return
            recursive(left)
        if right:
            if lst[midx] == '0' and '1' in right:
                cant = True
                return
            recursive(right)

    ans = [0] * len(numbers)
    for idx, num in enumerate(numbers):
        bi, blen, h = bin(num)[2:], len(bin(num)[2:]), 1
        while (1 << h) - 1 < blen:
            h += 1
        tlen = (1 << h) - 1
        bi = bi.zfill(tlen)

        cant = False
        recursive(bi)
        ans[idx] = int(not cant)

    return ans