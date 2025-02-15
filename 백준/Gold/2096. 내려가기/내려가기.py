def solution(N, numbers):
    mn, mx = [*numbers[0]], [*numbers[0]]
    for row in range(1, N):
        cmn, cmx = [*mn], [*mx]
        for col in range(3):
            if col == 0:
                mn[0] = numbers[row][col] + min(cmn[:-1])
                mx[0] = numbers[row][col] + max(cmx[:-1])
            elif col == 1:
                mn[1] = numbers[row][col] + min(cmn)
                mx[1] = numbers[row][col] + max(cmx)
            else:
                mn[2] = numbers[row][col] + min(cmn[1:])
                mx[2] = numbers[row][col] + max(cmx[1:])

    return f'{max(mx)} {min(mn)}'

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, numbers))