from collections import deque

drow = [0, 0, -1, 0 , 1, 0]
dcol = [0, 0, 0, 1, 0, -1]
dheight = [1, -1, 0, 0, 0, 0]

def solution(m, n, h, boxes):
    queue = deque()
    for height in range(h):
        for row in range(n):
            for col in range(m):
                if boxes[height][row][col] == 1:
                    queue.append((height, row, col))

    while queue:
        height, row, col = queue.popleft()
        for d in range(6):
            nheight = height + dheight[d]
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nheight < h) and (0 <= nrow < n) and (0 <= ncol < m):
                if boxes[nheight][nrow][ncol] == 0:
                    boxes[nheight][nrow][ncol] = boxes[height][row][col] + 1
                    queue.append((nheight, nrow, ncol))

    answer = 0
    for height in range(h):
        for row in range(n):
            for col in range(m):
                if boxes[height][row][col] == 0:
                    return -1
                answer = max(answer, boxes[height][row][col])

    return answer - 1

m, n, h = map(int, input().split())
boxes = []
for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    boxes.append(box)
print(solution(m, n, h, boxes))
