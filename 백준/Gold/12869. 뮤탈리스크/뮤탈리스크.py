from collections import deque

def solution(N, nums):

    def backtrack(n, lst, check):
        if n == N:
            possible.append([*lst])
            return
        for idx in range(N):
            if not check[idx]:
                check[idx] = 1
                lst.append(idx)
                backtrack(n + 1, lst, check)
                lst.pop()
                check[idx] = 0

    possible = []
    score = [9, 3, 1]
    backtrack(0, [], [0] * N)

    while len(nums) < 3:
        nums.append(0)

    queue = deque()
    a, b, c = nums
    queue.append((a, b, c, 0))
    check = {(a, b, c)}

    while queue:
        x, y, z, cnt = queue.popleft()
        if x <= 0 and y <= 0 and z <= 0:
            return cnt

        for perm in possible:
            nx, ny, nz = x, y, z
            damage = [0, 0, 0]
            for i in range(N):
                damage[perm[i]] = score[i]
            nx = max(0, nx - damage[0])
            ny = max(0, ny - damage[1])
            nz = max(0, nz - damage[2])

            state = (nx, ny, nz)
            if state not in check:
                check.add(state)
                queue.append((nx, ny, nz, cnt + 1))

    return -1

N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))