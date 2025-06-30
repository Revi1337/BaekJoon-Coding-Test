import sys
sys.setrecursionlimit(10**5)

memo = {}
memo[0], memo[1], memo[2] = 0, 1, 1

def solution(i):
    if i not in memo:
        if i%2==0:
            memo[i] = (solution(i//2) * (solution(i//2) + 2*solution(i//2-1)))%1_000_000_007
        else:
            memo[i] = (solution(i//2)**2 + solution(i//2+1)**2)%1_000_000_007
    return memo[i]

n = int(input())
print(solution(n))
