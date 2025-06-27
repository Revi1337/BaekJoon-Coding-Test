"""
1. 지수 법칙
2. 분배 법칙
3. 분할 정복
"""
def solution(A, B, C):
    if B == 1:
        return A % C
    ans = solution(A, B // 2, C)
    if B % 2 == 1:
        return ((ans * ans) % C) * A % C
    return (ans * ans) % C

A, B, C = map(int, input().split())
print(solution(A, B, C))
