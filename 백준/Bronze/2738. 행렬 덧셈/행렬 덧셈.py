def solution(n, m):
    answer = []
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        pre = []
        for j in range(m):
            pre.append(a[i][j] + b[i][j])
        answer.append(pre)
    for val in answer:
        print(" ".join(map(str, val)))


n, m = map(int, input().split())
solution(n, m)
