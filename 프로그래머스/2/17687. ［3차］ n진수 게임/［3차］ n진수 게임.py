def solution(n, t, m, p):
    p -= 1
    num, string = 0, '0'

    while len(string) <= m * (t + 1):
        curr, tmp = num, []
        while curr != 0:
            if 10 <= (curr % n) <= 15:
                tmp.append(chr(((curr % n - 10) + 65)))
            else:
                tmp.append(curr % n)
            curr //= n

        string += "".join(map(str, tmp[::-1]))
        num += 1

    ans = []
    for idx in range(len(string)):
        if idx % m == p:
            ans.append(string[idx])
        if len(ans) == t:
            break

    return ''.join(ans)