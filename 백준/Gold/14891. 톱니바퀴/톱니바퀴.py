from collections import deque

def solution(wheels, K, info):
    wheels = [deque(w) for w in wheels]
    left, right = 6, 2

    for w, d in info:
        w -= 1
        directions = [0] * 4
        directions[w] = d

        for i in range(w - 1, -1, -1):
            if wheels[i][right] != wheels[i + 1][left]:
                directions[i] = -directions[i + 1]
            else:
                break

        for i in range(w + 1, 4):
            if wheels[i - 1][right] != wheels[i][left]:
                directions[i] = -directions[i - 1]
            else:
                break

        for i in range(4):
            if directions[i] != 0:
                wheels[i].rotate(directions[i])

    answer = 0
    for i in range(4):
        if wheels[i][0] == 1:
            answer += (1 << i)

    return answer

wheels = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
info = [list(map(int, input().split())) for _ in range(K)]
print(solution(wheels, K, info))