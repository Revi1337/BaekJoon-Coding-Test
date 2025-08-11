import sys

input = sys.stdin.readline

def solution(D):
    arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 25, 30, 35, 28, 27, 26, 22, 24]
    idxes = [[1], [2], [3], [4], [5], [6, 22], [7], [8], [9], [10], [11, 31], [12], [13], [14], [15], [16, 28], [17], [18], [19], [20], [21], [21], [23], [24], [25], [26], [27], [20], [29], [30], [25], [32], [25]]
    horse = [0] * 4
    END = 21
    rot = {5, 10, 15}

    def backtrack(n, sm):
        if n == 10:
            nonlocal ans
            ans = max(ans, sm)
            return

        for h in range(4):
            if horse[h] == END:
                continue

            rollback = horse[h]
            cidx = None
            if horse[h] in rot:
                cidx = idxes[horse[h]][-1]
            else:
                cidx = idxes[horse[h]][0]

            for _ in range(D[n] - 1):
                cidx = idxes[cidx][0]
                if cidx == END:
                    break

            if cidx == END or cidx not in horse:
                horse[h] = cidx
                backtrack(n + 1, sm + arr[cidx])
                horse[h] = rollback

    ans = 0
    backtrack(0, 0)

    return ans

D = list(map(int, input().split()))
print(solution(D))
