def solution(N, T, B):
    bus = []
    for S, I, C in B:
        bus.append(S)
        for off in range(1, C):
            bus.append(S + I * off)

    bus.sort()
    length = len(bus)
    left, right = 0, length
    while left < right:
        mid = (left + right) // 2
        if bus[mid] < T:
            left = mid + 1
        else:
            right = mid

    return -1 if right == length else bus[right] - T


N, T = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, T, B))