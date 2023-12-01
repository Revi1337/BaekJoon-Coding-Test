lst = ["dz=", "c-", "d-", "lj", "nj", "s=", "z=", "c="]

def solution(string: str):
    cache = string
    answer = 0
    for val in lst:
        if val in cache:
            answer += cache.count(val)
            cache = cache.replace(val, '0')
    cache = cache.replace('0', '')
    answer += len(cache)
    return answer

print(solution(input()))

