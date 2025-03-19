def solution(n, times):
    
    def valid(time):
        sm = 0
        for t in times:
            sm += time // t
            if sm >= n:
                return True
        return False
    
    times.sort()
    left, right = 1, times[-1] * n
    answer = 1e11
    
    while left < right:
        mid = (left+right) // 2
        if not valid(mid):
            left = mid + 1
        else:
            answer = mid
            right = mid
    return answer