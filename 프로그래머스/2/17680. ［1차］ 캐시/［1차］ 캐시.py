from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache, ans = deque(), 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            ans += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            ans += 5

    return ans