def solution(clothes):
    cache = {}
    for _, kind in clothes:
        cache[kind] = cache.get(kind, 0) + 1
        
    answer = 1
    for _, cnt in cache.items():
        answer *= cnt + 1
        
    return answer - 1