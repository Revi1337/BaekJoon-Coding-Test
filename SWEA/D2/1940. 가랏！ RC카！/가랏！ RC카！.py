def solution(idx, N, C):
    psum = [0] * (N + 1)
    for sec, command in enumerate(C, start=1):
        if len(command) == 2:
            if command[0] == 1:
                psum[sec] = psum[sec - 1] + command[1]
            elif command[0] == 2:
                tmp = psum[sec - 1] - command[1]
                if tmp < 0:
                    psum[sec] = 0
                else:
                    psum[sec] += tmp
        else:
            psum[sec] = psum[sec - 1]
    return f'#{idx} {sum(psum)}'

T = int(input())
for idx in range(T):
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]
    print(solution(idx + 1, N, C))
