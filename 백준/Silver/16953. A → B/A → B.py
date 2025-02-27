from collections import deque

def solution(A, B):
    queue = deque([(B, 0)])
    while queue:
        num, cnt = queue.popleft()
        if num == A:
            return cnt + 1
        if not num % 2:
            queue.append((num // 2, cnt + 1))
        if str(num)[-1] == '1' and str(num)[:-1] != '':
            queue.append((int(str(num)[:-1]) , cnt + 1))

    return -1

A, B = map(int, input().split())
print(solution(A, B))

