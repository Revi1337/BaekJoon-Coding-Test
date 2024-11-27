def solution(N, pos):
    paper = [[-1] * 1001 for _ in range(1001)]
    for idx, (x, y, width, height) in enumerate(pos):
        for row in range(y, y + height):
            for col in range(x, x + width):
                paper[row][col] = idx

    answer = [0] * N
    for line in paper:
        for val in line:
            if val != -1:
                answer[val] += 1

    for ans in answer:
        print(ans)

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
solution(N, pos)
