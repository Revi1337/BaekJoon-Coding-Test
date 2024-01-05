import sys

def solution(data):
    n, k = data[0], data[1]
    arr = [i for i in range(1, n + 1)]
    answer = []
    idx = 0
    for i in range(n):
        idx += k - 1
        if idx >= len(arr):
            idx %= len(arr)
        answer.append(str(arr.pop(idx)))
    return '<' + ", ".join(answer) + '>'

print(solution(list(map(int, sys.stdin.readline().rstrip().split()))))

