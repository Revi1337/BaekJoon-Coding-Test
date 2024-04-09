import sys

input = sys.stdin.readline

def solution(n, m, videos):
    answer = float('inf')
    left, right = max(videos), sum(videos)
    while left <= right:
        mid = (left + right) // 2
        sum_num = 0
        counter = 1
        for video in videos:
            if sum_num + video <= mid:
                sum_num += video
            else:
                counter += 1
                sum_num = video
        if counter > m:
            left = mid + 1
        else:
            if mid < answer:
                answer = mid
            right = mid - 1
    return answer

n, m = map(int, input().split())
videos = list(map(int, input().split()))
print(solution(n, m, videos))
