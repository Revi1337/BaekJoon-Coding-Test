def solution(n):
     return sum(filter(lambda x: x % 2 == 0, range(1,n+1)))