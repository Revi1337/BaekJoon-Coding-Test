from collections import deque

# 위, 아래, 앞, 뒤, 좌, 우
dhei = [-1, 1, 0, 0, 0, 0]
drow = [0, 0, -1, 1, 0, 0]
dcol = [0, 0, 0, 0, -1, 1]

def solution(plts):

    def inside(h, r, c):
        return 0 <= h < 5 and 0 <= r < 5 and 0 <= c < 5

    def place(lst, check):
        if len(lst) == 5:
            poss.append(lst[:])
            return
        for num in range(5):
            if not check[num]:
                check[num] = 1
                lst.append(num)
                place(lst, check)
                lst.pop()
                check[num] = 0

    def rotation(lst):
        if len(lst) == 5:
            rots.append(lst[:])
            return
        for num in range(4):
            lst.append(num)
            rotation(lst)
            lst.pop()

    def rot(plt, cnt):
        for _ in range(cnt):
            p = [[0] * 5 for _ in range(5)]
            for idx in range(5):
                for jdx in range(5):
                    p[jdx][4 - idx] = plt[idx][jdx]
            plt = p
        return plt

    def bfs(plates, start):
        sh, sr, sc = start
        if plates[sh][sr][sc] == 0:
            return -1
        check = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        check[sh][sr][sc] = 1
        queue = deque([(sh, sr, sc)])
        while queue:
            h, r, c = queue.popleft()
            if (h, r, c) == (4, 4, 4):
                return check[h][r][c] - 1
            for d in range(6):
                nh, nr, nc = h + dhei[d], r + drow[d], c + dcol[d]
                if inside(nh, nr, nc) and not check[nh][nr][nc] and plates[nh][nr][nc]:
                    check[nh][nr][nc] = check[h][r][c] + 1
                    queue.append((nh, nr, nc))
        return -1

    poss, rots = [], []
    place([], [0] * 5), rotation([])
    ans = float('inf')

    for seq in poss:
        for case in rots:
            plates = []
            for i in range(5):
                plates.append(rot(plts[seq[i]], case[i]))
            if plates[0][0][0] and plates[4][4][4]:
                res = bfs(plates, (0, 0, 0))
                if res != -1:
                    ans = min(ans, res)

    return ans if ans != float('inf') else -1

plts = []
for _ in range(5):
    plts.append([list(map(int, input().split())) for _ in range(5)])
print(solution(plts))