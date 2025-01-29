def solution(M, tstars, N, stars):
    stars = set(map(tuple, stars))
    for tcol, trow in tstars:
        for col, row in stars:
            dcol, drow = col - tcol, row - trow

            for tcol2, trow2 in tstars:
                ncol, nrow = tcol2 + dcol, trow2 + drow
                if (ncol, nrow) not in stars:
                    break
            else:
                print(dcol, drow)
                break
        break


M = int(input())
stars = [list(map(int, input().split())) for _ in range(M)]
N = int(input())
tstars = [list(map(int, input().split())) for _ in range(N)]
solution(M, stars, N, tstars)