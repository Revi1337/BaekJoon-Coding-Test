from collections import deque

directions = {(1, 0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0): 'u'}

def solution(n, m, x, y, r, c, k):
    
    def manhattan(row, col):
        return abs(row - r) + abs(col- c)
    
    x, y = x - 1, y - 1
    r, c = r - 1, c - 1
    
    if manhattan(x, y) > k or (manhattan(x, y) - k) % 2:
        return 'impossible'

    queue = deque([(x, y, 0, '')])
    while queue:
        row, col, cnt, path = queue.popleft()
        if (row, col) == (r, c) and (k - cnt) % 2:
            return 'impossible'
        elif (row, col) == (r, c) and cnt == k:
            return path
        for (rr, cc), dir in directions.items():
            nrow, ncol = row + rr, col + cc
            if not (0 <= nrow < n and 0 <= ncol < m):
                continue
            if manhattan(nrow, ncol) + cnt + 1 > k:
                continue
            queue.append((nrow, ncol, cnt + 1, path + dir))
            break

