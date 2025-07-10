drow = [0, -1, -1, -1, 0, 1, 1, 1]
dcol = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상 좌 하 우
sdrow = [-1, 0, 1, 0]
sdcol = [0, -1, 0, 1]

def solution(M, S, fishes, srow, scol):

    inside = lambda row, col: 0 <= row < 4 and 0 <= col < 4

    def shark_pos():
        sdirs = []
        def poss(lst):
            if len(lst) == 3:
                sdirs.append([*lst])
                return lst
            for num in [0, 1, 2, 3]: # 사전순으로 미리 좌표들 생성
                lst.append(num)
                poss(lst)
                lst.pop()

        poss([])
        return sdirs

    srow, scol = srow - 1, scol - 1
    FI, SM, sdirs = {}, {}, shark_pos()
    for row, col, d in fishes:
        row, col, d = row - 1, col - 1, d - 1
        pos = (row, col)
        FI[pos] = FI.get(pos, [])
        FI[pos].append(d)

    for t in range(S):
        NFI = {}
        for pos, cdirs in FI.items(): # 물고기 이동
            row, col = pos
            for cd in cdirs:
                for _ in range(8):
                    nd = (cd - _) % 8
                    nrow, ncol = row + drow[nd], col + dcol[nd]
                    if inside(nrow, ncol) and (nrow, ncol) not in SM and (nrow != srow or ncol != scol):
                        NFI[(nrow, ncol)] = NFI.get((nrow, ncol), [])
                        NFI[(nrow, ncol)].append(nd)
                        break
                else:
                    NFI[(row, col)] = NFI.get((row, col), [])
                    NFI[(row, col)].append(cd)

        mx, poss = -1, []
        for dd in sdirs: # 상어 이동
            ssrow, sscol, tmp, pos = srow, scol, 0, []
            check = set()
            for nd in dd:
                nrow, ncol = ssrow + sdrow[nd], sscol + sdcol[nd]
                if not inside(nrow, ncol):
                    break
                npos = (nrow, ncol)
                if npos in NFI and npos not in check:  # 중복 제거 방지
                    tmp += len(NFI[npos])
                    check.add(npos)
                    pos.append([nrow, ncol, 1])
                else:
                    pos.append([nrow, ncol, 0])
                ssrow, sscol = nrow, ncol
            else:
                if tmp > mx:
                    mx, poss = tmp, pos
        srow, scol, _ = poss[-1] # 상어 좌표 이동 (mx 초기값이 -1 이었으니, 무조건 값이 있음. 실제론 0이 최소이기 때문에)

        for row, col, f in poss:
            if f:
                pos = (row, col)
                NFI.pop(pos) # 다음 물고기들에서 물고기들을 제외
                SM[pos] = t # 냄새를 뭍힘 (이미 냄새가 있어도, 기존 냄새를 최신으로 반영)

        SM = {pos: time for pos, time in SM.items() if time != t - 2}  # 두 번 전 냄새들 제거

        for pos, ddirs in NFI.items(): # 복제 적용
            if pos in FI:
                FI[pos].extend([*ddirs])
            else:
                FI[pos] = FI.get(pos, [])
                FI[pos].extend([*ddirs])

    return sum(len(FI[pos]) for pos in FI)

M, S = map(int, input().split())
fishes = [list(map(int, input().split())) for _ in range(M)]
srow, scol = map(int, input().split())
print(solution(M, S, fishes, srow, scol))