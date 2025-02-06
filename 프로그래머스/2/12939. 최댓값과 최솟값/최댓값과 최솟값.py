def solution(s):
    s = list(map(int, s.split()))
    mx, mn = max(s), min(s)
    return " ".join(map(str, [mn, mx]))