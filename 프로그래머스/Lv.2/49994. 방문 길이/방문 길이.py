row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

def solution(dirs):
    r = c = 0
    dr = dc = 0
    answer = set()
    for dir in dirs:
        if dir == 'U':
            dr = r + row[0]
            dc = c + col[0]
        elif dir == 'R':
            dr = r + row[1]
            dc = c + col[1]
        elif dir == 'D':
            dr = r + row[2]
            dc = c + col[2]
        elif dir == 'L':
            dr = r + row[3]
            dc = c + col[3]

        if not ((-5 <= dr <= 5) and (-5 <= dc <= 5)):
            continue

        answer.add((c, r, dc, dr))
        answer.add((dc, dr, c, r))

        c, r = dc, dr

    return len(answer) // 2