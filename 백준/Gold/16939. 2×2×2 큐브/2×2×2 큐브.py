def solution(cube):

    def check(cube):
        for idx in range(0, 24, 4):
            if len(set(cube[idx: idx + 4])) != 1:
                return False
        return True

    def left_left(cube):
        cc = [*cube]
        cc[0], cc[2], cc[4], cc[6], cc[8], cc[10], cc[23], cc[21] = \
            cc[4], cc[6], cc[8], cc[10], cc[23], cc[21], cc[0], cc[2]
        return cc

    def left_right(cube):
        cc = [*cube]
        cc[0], cc[2], cc[4], cc[6], cc[8], cc[10], cc[23], cc[21] = \
            cc[23], cc[21], cc[0], cc[2], cc[4], cc[6], cc[8], cc[10]
        return cc

    def right_right(cube):
        cc = [*cube]
        cc[1], cc[3], cc[5], cc[7], cc[9], cc[11], cc[22], cc[20] = \
            cc[5], cc[7], cc[9], cc[11], cc[22], cc[20], cc[1], cc[3]
        return cc

    def right_left(cube):
        cc = [*cube]
        cc[1], cc[3], cc[5], cc[7], cc[9], cc[11], cc[22], cc[20] = \
            cc[22], cc[20], cc[1], cc[3], cc[5], cc[7], cc[9], cc[11]
        return cc

    def behind_left(cube):
        cc = [*cube]
        cc[12], cc[13], cc[4], cc[5], cc[16], cc[17], cc[20], cc[21] = \
            cc[4], cc[5], cc[16], cc[17], cc[20], cc[21], cc[12], cc[13]
        return cc

    def behind_right(cube):
        cc = [*cube]
        cc[12], cc[13], cc[4], cc[5], cc[16], cc[17], cc[20], cc[21] = \
            cc[20], cc[21], cc[12], cc[13], cc[4], cc[5], cc[16], cc[17]
        return cc

    def front_left(cube):
        cc = [*cube]
        cc[14], cc[15], cc[6], cc[7], cc[18], cc[19], cc[22], cc[23] = \
            cc[6], cc[7], cc[18], cc[19], cc[22], cc[23], cc[14], cc[15]
        return cc

    def front_right(cube):
        cc = [*cube]
        cc[14], cc[15], cc[6], cc[7], cc[18], cc[19], cc[22], cc[23] = \
            cc[22], cc[23], cc[14], cc[15], cc[6], cc[7], cc[18], cc[19]
        return cc

    def top_left(cube):
        cc = [*cube]
        cc[2], cc[3], cc[16], cc[18], cc[9], cc[8], cc[15], cc[13] = \
            cc[16], cc[18], cc[9], cc[8], cc[15], cc[13], cc[2], cc[3]
        return cc

    def top_right(cube):
        cc = [*cube]
        cc[2], cc[3], cc[16], cc[18], cc[9], cc[8], cc[15], cc[13] = \
            cc[15], cc[13], cc[2], cc[3], cc[16], cc[18], cc[9], cc[8]
        return cc

    def bottom_left(cube):
        cc = [*cube]
        cc[0], cc[1], cc[17], cc[19], cc[11], cc[10], cc[14], cc[12] = \
            cc[17], cc[19], cc[11], cc[10], cc[14], cc[12], cc[0], cc[1]
        return cc

    def bottom_right(cube):
        cc = [*cube]
        cc[0], cc[1], cc[17], cc[19], cc[11], cc[10], cc[14], cc[12] = \
            cc[14], cc[12], cc[0], cc[1], cc[17], cc[19], cc[11], cc[10]
        return cc

    check(cube)

    for callable in [left_left, left_right, right_right, right_left, behind_left, behind_right, front_left, front_right, top_left, top_right, bottom_left, bottom_right]:
        cc = callable(cube)
        if check(cc):
            return 1
    return 0


cube = list(map(int, input().split()))
print(solution(cube))