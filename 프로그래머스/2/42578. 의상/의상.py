def solution(clothes):
    cache = {}
    for _, kind in clothes:
        cache[kind] = cache.get(kind, 0) + 1
        
    answer = 1
    for _, cnt in cache.items():
        answer *= cnt + 1
        
    return answer - 1


# def solution(clothes):

#     def backtracking(n, cnt):
#         if n == length:
#             nonlocal answer
#             if cnt:
#                 answer += 1
#             return

#         cloth, kind = clothes[n]
#         backtracking(n + 1, cnt)

#         if kind not in cache:
#             cache.add(kind)
#             backtracking(n + 1, cnt + 1)
#             cache.discard(kind)

#     answer, length, cache = 0, len(clothes), set()
#     backtracking(0, 0)

#     return answer
