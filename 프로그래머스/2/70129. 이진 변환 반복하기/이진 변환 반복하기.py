def solution(s):
    ans = [0] * 2
    while s != '1':
        cnt = s.count('0')
        length = len(s) - cnt
        after = bin(length)[2:]

        ans[0] += 1
        ans[1] += cnt
        s = after

    return ans