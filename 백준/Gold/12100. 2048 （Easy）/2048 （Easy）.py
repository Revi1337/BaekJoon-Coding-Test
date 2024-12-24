"""
목표 : 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구해라.

1. 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
2. 한번 합쳐진 블록은 다시 합쳐질 수 없다.
3. 똑같은 수가 세개 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.

만약 (상) 방향이면 좌표를 합치고, 해당 블록을 상으로 옮겨야한다. 

예상 행복회로..
4진 탐색

def backtracking(n, arr):
    if n == 5:
        최종 arr 를 탐색 후, 최대값을 갱신.
        return

    복사된 배열  = 복사(배열)

    위로 회전 (복사된 배열)
    backtracking(n + 1, 위로 회전된 배열)
    좌로 회전 (복사된 배열)
    backtracking(n + 1, 좌로 회전된 배열)
    하로 회전 (복사된 배열)
    backtracking(n + 1, 하로 회전된 배열)
    좌로 회전 (복사된 배열)
    backtracking(n + 1, 좌로 회전된 배열)
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    def up(arr):
        m_arr = [[*line] for line in arr]
        for col in range(N):
            gap = 0
            for row in range(N):
                if m_arr[row][col] != 0:
                    tmp = arr[row][col]
                    m_arr[row][col] = 0
                    if m_arr[gap][col] == 0:
                        m_arr[gap][col] = tmp
                    elif m_arr[gap][col] == tmp:
                        m_arr[gap][col] *= 2
                        gap += 1
                    else:
                        gap += 1
                        m_arr[gap][col] = tmp
        return m_arr

    def right(arr):
        m_arr = [[*line] for line in arr]
        for row in range(N):
            gap = N - 1
            for j in range(N - 1, -1, -1):
                if m_arr[row][j] != 0:
                    tmp = m_arr[row][j]
                    m_arr[row][j] = 0
                    if m_arr[row][gap] == 0:
                        m_arr[row][gap] = tmp
                    elif m_arr[row][gap] == tmp:
                        m_arr[row][gap] *= 2
                        gap -= 1
                    else:
                        gap -= 1
                        m_arr[row][gap] = tmp
        return m_arr

    def down(arr):
        m_arr = [[*line] for line in arr]
        for col in range(N):
            gap = N - 1
            for row in range(N - 1, -1, -1):
                if m_arr[row][col] != 0:
                    tmp = m_arr[row][col]
                    m_arr[row][col] = 0
                    if m_arr[gap][col] == 0:
                        m_arr[gap][col] = tmp
                    elif m_arr[gap][col] == tmp:
                        m_arr[gap][col] *= 2
                        gap -= 1
                    else:
                        gap -= 1
                        m_arr[gap][col] = tmp
        return m_arr


    def left(arr):
        m_arr = [[*line] for line in arr]
        for row in range(N):
            gap = 0
            for col in range(1, N):
                if m_arr[row][col] != 0:
                    tmp = m_arr[row][col]
                    m_arr[row][col] = 0
                    if m_arr[row][gap] == 0:
                        m_arr[row][gap] = tmp
                    elif m_arr[row][gap] == tmp:
                        m_arr[row][gap] *= 2
                        gap += 1
                    else:
                        gap += 1
                        m_arr[row][gap] = tmp
        return m_arr

    def backtracking(n, arr):
        if n == 5:
            nonlocal answer
            for row in range(N):
                for col in range(N):
                    answer = max(answer, arr[row][col])
            return

        carr = [[*line] for line in arr]

        backtracking(n + 1, up(carr))
        backtracking(n + 1, right(carr))
        backtracking(n + 1, down(carr))
        backtracking(n + 1, left(carr))

    answer = -1e9
    backtracking(0, arr)

    return answer

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))