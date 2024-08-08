import sys

input = sys.stdin.readline

'''
30 (https://www.acmicpc.net/problem/10610)
'''

def solution(N):
    N = str(N)
    if "0" not in N:
        print(-1)
        return
    num_sum = 0
    for i in range(len(N)):
        num_sum += int(N[i])

    if num_sum % 3 != 0:
        print(-1)

    else:
        sorted_num = sorted(N, reverse=True)
        answer = "".join(sorted_num)
        print(answer)

N = int(input())
solution(N)
