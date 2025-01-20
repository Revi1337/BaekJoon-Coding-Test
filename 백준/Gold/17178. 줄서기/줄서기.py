from collections import deque

def solution(N, lines):
    wait, lines = [], deque([lines[row][col] for row in range(N) for col in range(5)])
    tmp_lines = [[line.split('-')[0], int(line.split('-')[1])] for line in lines]
    tmp_lines.sort()
    slines = []
    for alpha, num in tmp_lines:
        num = str(num)
        slines.append(alpha + '-' + num)

    for curr in slines:
        if lines and lines[0] == curr:
            lines.popleft()
            continue
        if wait and wait[-1] == curr:
            wait.pop()
            continue

        while lines and lines[0] != curr:
            wait.append(lines.popleft())

        if not lines or lines[0] != curr:
            return "BAD"
        lines.popleft()

    return 'GOOD'

N = int(input())
lines = [input().rstrip().split() for _ in range(N)]
print(solution(N, lines))