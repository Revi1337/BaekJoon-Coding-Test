def solution(s):
    mn = len(s)
    for length in range(1, len(s) // 2 + 1):
        comp = ""
        prev = s[:length]
        cnt = 1
        for idx in range(length, len(s), length):
            curr = s[idx:idx + length]
            if curr == prev:
                cnt += 1
            else:
                comp += (str(cnt) + prev) if cnt > 1 else prev
                prev = curr
                cnt = 1

        comp += (str(cnt) + prev) if cnt > 1 else prev
        mn = min(mn, len(comp))

    return mn