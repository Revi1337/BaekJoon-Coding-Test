def solution(N, pos):
    paper = [[0] * 102 for _ in range(102)]

    for x, y in pos:
        for row in range(y + 1, y + 11):
            for col in range(x + 1, x + 11):
                paper[row][col] = 1

    rev_paper = list(zip(*paper))

    answer = 0
    for line in paper:
        for idx in range(1, len(line)):
            if line[idx] != line[idx - 1]:
                answer += 1

    for line in rev_paper:
        for idx in range(1, len(line)):
            if line[idx] != line[idx - 1]:
                answer += 1

    return answer


N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, pos))