def solution(idx, v1, v2, v3, v4):
    cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if v3 == v1:
        return f'#{idx} {v4 - v2 + 1}'
    total = cal[v1] - v2 + v4 + 1
    for wal in range(v1 + 1, v3):
        total += cal[wal]
    return f'#{idx} {total}'

T = int(input())
for idx in range(T):
    v1, v2, v3, v4 = map(int, input().split())
    print(solution(idx + 1, v1, v2, v3, v4))

