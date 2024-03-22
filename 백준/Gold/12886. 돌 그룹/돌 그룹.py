from collections import deque
import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(A, B, C):
    total = sum([A, B, C])
    check = [[0] * (total + 1) for _ in range(total + 1)]
    queue = deque([(A, B)])
    while queue:
        a, b = queue.popleft()
        c = total - sum([a, b])
        if a == b == c:
            return 1
        for na, nb in [(a, b), (b, c), (c, a)]:
            if na == nb:
                continue
            if na > nb:
                na, nb = nb, na
            na, nb = na * 2, nb - na
            min_num = min(na, nb, total - (na + nb))
            max_num = max(na, nb, total - (na + nb))
            if not check[min_num][max_num]:
                check[min_num][max_num] = 1
                queue.append((min_num, max_num))
    return 0

a, b, c = map(int, input().split())
print(solution(a, b, c))