import sys

input = sys.stdin.readline

def solution(N, Q, integers, operations):
    left = 0
    for operation in operations:
        if operation[0] == 1:
            target = (left + (operation[1] - 1)) % N
            integers[target] += operation[2]
        elif operation[0] == 2:
            left = (left - operation[1]) % N
        elif operation[0] == 3:
            left = (left + operation[1]) % N

    print(*integers[left:], *integers[:left], sep=' ')

N, Q = map(int, input().split())
integers = list(map(int, input().split()))
operations = [list(map(int, input().split())) for _ in range(Q)]
solution(N, Q, integers, operations)
