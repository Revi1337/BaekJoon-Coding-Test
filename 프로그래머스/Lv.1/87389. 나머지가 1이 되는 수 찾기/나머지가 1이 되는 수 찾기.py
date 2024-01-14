def solution(n):
    must = n - 1
    for integer in range(2, must // 2 + 1):
        if not must % integer:
            return integer
    return must