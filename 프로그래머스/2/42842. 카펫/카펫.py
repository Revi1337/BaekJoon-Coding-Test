def solution(brown, yellow):
    answer = []
    weight = brown + yellow
    cache = {brown, yellow}
    for row in range(3, int((weight) ** 0.5) + 1):
        if not weight % row:
            col = weight // row
            if row * 2 + col * 2 - 4 in cache:
                return [max(row, col), min(row, col)]
            