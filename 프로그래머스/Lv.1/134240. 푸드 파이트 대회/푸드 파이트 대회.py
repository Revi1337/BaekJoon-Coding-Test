from collections import deque

def solution(foods):
    h1 = []
    h2 = deque()
    length = len(foods)
    for idx in range(length):
        cnt = foods[idx]
        while cnt > 1:
            if cnt // 2:
                h1.append(str(idx))
                h2.appendleft(str(idx))
                cnt -= 2
    h1.append('0')
    h1.extend(h2)
    return "".join(h1)