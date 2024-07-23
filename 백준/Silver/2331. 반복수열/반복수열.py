import sys

input = sys.stdin.readline

def solution(A, P):
    cache = {str(A)}
    answer = [str(A)]
    dup = None
    curr = str(A)
    while True:
        pre = 0
        for integer in curr:
            pre += int(integer) ** P
        if str(pre) not in cache:
            cache.add(str(pre))
            answer.append(str(pre))
            curr = str(pre)
        else:
            dup = str(pre)
            break

    for idx in range(len(answer)):
        if answer[idx] == dup:
            return len(answer[:idx])

A, P = map(int, input().split())
print(solution(A, P))