"""
1. 인접한 idx 끼리의 sub 를 구한다. (이미 정렬된 상태)
2. sub 들을 sort() 하고 sum(diff[:N - K]) 를 리턴한다.

1   3   5   5   7   10  (그룹 3개)  
  2   2   0   2   3
(1,3), (5,5,7), (10) = 4
(1,3,5,5), (7), (10) = 4
(1), (3,5,5,7), (10) = 4
"""
def solution(N, K, heights):
    diff = [0] * (N - 1)
    for idx in range(N - 1):
        diff[idx] = heights[idx + 1] - heights[idx]

    diff.sort()
    return sum(diff[:N - K])

N, K = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(N, K, heights))
