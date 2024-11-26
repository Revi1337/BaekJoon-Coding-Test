def solution(N, pos):
    paper = [[0] * 100 for _ in range(100)]
    for x, y in pos:
        for row in range(y, y + 10):
            for col in range(x, x + 10):
                paper[row][col] = 1

    return sum([val for line in paper for val in line])

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, pos))

