ARCH = 3

def solution(N, M, D, board):

    CASTLE_ROW = N

    def combination(n, st, lst):
        if n == ARCH:
            arch_pos.append([*lst])
            return

        for num in range(st, M):
            combination(n + 1, num + 1, lst + [(CASTLE_ROW, num)])

    arch_pos = []
    combination(0, 0, [])

    answer = 0
    for archs in arch_pos:
        enemies = set((row, col) for row in range(N) for col in range(M) if board[row][col])
        total_kill = 0

        while enemies:
            kill = set()
            s_enemies = sorted(enemies, key=lambda x: (x[1], x[0]))
            for ar, ac in archs:
                target = None
                min_dist = D + 1
                for erow, ecol in s_enemies:
                    dist = abs(ar - erow) + abs(ac - ecol)
                    if dist <= D:
                        if dist < min_dist:
                            min_dist = dist
                            target = (erow, ecol)
                if target:
                    kill.add(target)

            total_kill += len(kill)
            enemies -= kill

            new_enemies = set()
            for erow, ecol in enemies:
                if erow + 1 < N:
                    new_enemies.add((erow + 1, ecol))
            enemies = new_enemies

        answer = max(answer, total_kill)

    return answer


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, D, board))
