import sys

input = sys.stdin.readline

"""
N-Queen (https://www.acmicpc.net/problem/9663)
2024-09-16
"""

def solution(N):

    """
    check2, check3 == 대각선
    check2 는 row + col 이라 2N 인건 이해가능
    check3 는 row - col 인데, - 일 수 있고, + 일 수 있기 때문에, 2N 을 해야함. + 일땐 앞에서 부터 양수 인덱스 체크, - 일때는 뒤에서부터 인덱스 체크 함.
            [0,0,0,0    0,0,0,0]
            (+) -->      <-- (-)
    """
    def recursive(depth):
        if depth == N:
            nonlocal answer
            answer += 1
            return
        for nc in range(N):
            if check1[nc] == check2[depth + nc] == check3[depth - nc] == 0:
                check1[nc] = check2[depth + nc] = check3[depth - nc] = 1
                recursive(depth + 1)
                check1[nc] = check2[depth + nc] = check3[depth - nc] = 0

    answer = 0
    check1 = [0] * N
    check2, check3 = [[0] * (2 * N) for _ in range(2)]
    recursive(0)
    print(answer)

N = int(input())
solution(N)