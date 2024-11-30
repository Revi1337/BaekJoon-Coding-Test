def solution(squares):
    sj1, si1, ej1, ei1, sj2, si2, ej2, ei2 = squares
    if si1 > ei2 or ei1 < si2 or sj1 > ej2 or ej1 < sj2:
        ans = 'd'
    elif ej1 == sj2 or sj1 == ej2:
        if ei1 == si2 or si1 == ei2:
            ans = 'c'
        else:
            ans = 'b'
    elif ei1 == si2 or si1 == ei2:
        ans = 'b'
    else:
        ans = 'a'

    return ans

for _ in range(4):
    squares = list(map(int, input().split()))
    print(solution(squares))
