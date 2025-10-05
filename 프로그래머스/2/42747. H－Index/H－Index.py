def solution(citations):
    citations.sort(reverse=True)
    ans = 0
    for idx, cnt in enumerate(citations):
        if cnt >= idx + 1:
            ans = idx + 1
        else:
            break
    return ans