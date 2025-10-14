drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, arr):
    WAT, ICE, BIRD = '.', 'X', 'L'

    inside = lambda row, col: 0 <= row < R and 0 <= col < C
    idx = lambda row, col: C * row + col

    def set_up():
        birds, ices = [], set()
        for row in range(R):
            for col in range(C):
                if arr[row][col] == BIRD:
                    birds.append((row, col))
                    arr[row][col] = WAT
                if arr[row][col] == ICE:
                    for d in range(4):
                        nrow, ncol = row + drow[d], col + dcol[d]
                        if inside(nrow, ncol) and arr[nrow][ncol] != ICE:
                            ices.add((row, col))
                            break
        return birds, ices

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 != root2:
            parents[root2] = root1

    birds, ices = set_up()
    b1, b2 = idx(*birds[0]), idx(*birds[1])
    parents = list(range(R * C))

    for row in range(R):
        for col in range(C):
            if arr[row][col] == WAT:
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if inside(nrow, ncol) and arr[nrow][ncol] == WAT:
                        union(idx(row, col), idx(nrow, ncol))

    if find(b1) == find(b2):
        return 0

    ans = 1
    while True:
        for row, col in ices:
            arr[row][col] = WAT

        nxt = set()
        for row, col in ices:
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol):
                    if arr[nrow][ncol] == WAT:
                        union(idx(row, col), idx(nrow, ncol))
                    elif arr[nrow][ncol] == ICE:
                        nxt.add((nrow, ncol))

        if find(b1) == find(b2):
            return ans

        ices = nxt
        ans += 1

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
print(solution(R, C, arr))