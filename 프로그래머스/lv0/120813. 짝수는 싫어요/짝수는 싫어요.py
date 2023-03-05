def solution(n):
    if n % 2 == 0:
        return list(range(1,n,2))
    else:
        return list(range(1,n+1,2))