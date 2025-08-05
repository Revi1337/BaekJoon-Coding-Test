import sys

input = sys.stdin.readline

def solution(N, OP):

    LIMIT = 1_000_000

    def find(n):
        if parents[n] == n:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
            cnts[r1] += cnts[r2]
        else:
            parents[r1] = r2
            cnts[r2] += cnts[r1]

    parents, cnts = list(range(LIMIT + 1)), [1] * (LIMIT + 1)
    for op, *lst, in OP:
        if op == 'I':
            n1, n2 = int(lst[0]), int(lst[1])
            r1, r2 = find(n1), find(n2)
            if r1 != r2:
                union(n1, n2)
        else:
            n = int(lst[0])
            print(cnts[find(n)])

N = int(input())
OP = [input().rstrip().split() for _ in range(N)]
solution(N, OP)
