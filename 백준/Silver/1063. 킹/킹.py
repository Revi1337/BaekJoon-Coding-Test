import sys

input = sys.stdin.readline

dir_dict = {
    'T': [1, 0],
    'RT': [1, 1],
    'R': [0, 1],
    'RB': [-1, 1],
    'B': [-1, 0],
    'LB': [-1, -1],
    'L': [0, -1],
    'LT': [1, -1],
}

"""
가는 방향에 돌이 있으면 돌이 경계선을 넘어가냐 안넘어가냐 체크
    안넘어가면 --> king, rock 포지션 둘다 업데이트한다.
    넘어가면 --> pass
    
가는방향에 돌이 없으면 king 만 경계선을 넘어가냐 안넘어가냐 체크
"""
def solution(king, rockp, _, operations) -> None:
    rock_row, rock_col = int(rockp[1]), ord(rockp[0])
    krow, kcol = int(king[1]), ord(king[0])
    for oper in operations:
        nrow, ncol = krow + dir_dict[oper][0], kcol + dir_dict[oper][1]
        if (nrow, ncol) == (rock_row, rock_col):
            rr = rock_row + dir_dict[oper][0]
            rc = rock_col + dir_dict[oper][1]
            if 1 <= rr <= 8 and 65 <= rc <= 72:
                rock_row, rock_col = rr, rc
                krow, kcol = nrow, ncol
        else:
            if 1 <= nrow <= 8 and 65 <= ncol <= 72:
                krow, kcol = nrow, ncol

    print(chr(kcol) + str(krow))
    print(chr(rock_col) + str(rock_row))


king, rockp, N = input().strip().split()
operations = [input().strip() for _ in range(int(N))]
solution(king, rockp, N, operations)