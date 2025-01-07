from collections import deque

def solution(T, wheels, K, dirs):
    left, right = 6, 2
    wheels = [deque(wheel) for wheel in wheels]
    for wn, dir in dirs:
        wn, directions = wn - 1, [0] * T

        directions[wn] = dir

        for idx in range(wn - 1, -1, -1):
            if wheels[idx][right] != wheels[idx + 1][left]:
                directions[idx] = directions[idx + 1] * -1
            else:
                break

        for idx in range(wn + 1, T):
            if wheels[idx][left] != wheels[idx - 1][right]:
                directions[idx] = directions[idx - 1] * -1
            else:
                break

        for idx in range(T):
            if directions[idx] != 0:
                wheels[idx].rotate(directions[idx])

    answer = 0
    for wheel in wheels:
        if wheel[0]:
            answer += 1

    return answer


T = int(input())
wheels = [list(map(int, input().rstrip())) for _ in range(T)]
K = int(input())
dirs = [list(map(int, input().split())) for _ in range(K)]
print(solution(T, wheels, K, dirs))
