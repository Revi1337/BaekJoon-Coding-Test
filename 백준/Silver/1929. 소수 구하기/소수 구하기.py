import sys

input = sys.stdin.readline

def solution(m, n):
    check = [0] * (n + 1)
    answer = []
    for integer in range(2, n + 1):
        if check[integer] == 0:
            answer.append(integer)
            for number in range(integer, n + 1, integer):
                check[number] = 1
    for integer in answer:
        if m <= integer <= n:
            print(integer)

m, n = map(int, input().split())
solution(m, n)