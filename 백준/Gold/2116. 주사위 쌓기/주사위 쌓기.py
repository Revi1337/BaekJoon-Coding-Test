direction = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

def solution(N, dices):

    def find_max(num):
        mx = 0
        for idx in range(N):
            for jdx in range(6):
                if dices[idx][jdx] == num:
                    down, up = num, dices[idx][direction[jdx]]
                    if 6 in {down, up}:
                        if 5 in {down, up}:
                            mx += 4
                        else:
                            mx += 5
                    else:
                        mx += 6
                    num = up
                    break
        return mx

    answer = 0
    for num in range(1, 7):
        answer = max(answer, find_max(num))

    return answer


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, dices))
