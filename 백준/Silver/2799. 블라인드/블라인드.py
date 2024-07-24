import sys

input = sys.stdin.readline

def solution(M, N, windows):
    answer = [0] * 5
    rlen = len(windows)
    clen = len(windows[0])
    for c in range(0, clen, 5):
        pre = []
        for r in range(0, rlen, 5):
            rows = windows[r : r + 5]
            rows = list(map(lambda x: x[c : c + 5], rows))
            for row in rows:
                pre.append(row[1:])
        pre.pop(0)
        counter = 0
        for p in pre:
            if p:
                string = "".join(p)
                if string == '####':
                    answer[counter] += 1
                    counter = 0
                elif string == '****':
                    counter += 1
    print(*answer, sep = ' ')

M, N = map(int, input().split())
windows = []
for _ in range(M):
    for _ in range(5):
        string = list(input().strip())
        windows.append(string)
string = list(input().strip())
windows.append(string)
solution(M, N, windows)