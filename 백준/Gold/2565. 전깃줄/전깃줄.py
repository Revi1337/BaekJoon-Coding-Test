def solution(N, wires):

    def bisect_left(target):
        left, right = 0, len(cache)
        while left < right:
            mid = (left + right) // 2
            if cache[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    wires.sort()
    positions = [b for _, b in wires]
    cache = []
    for b in positions:
        idx = bisect_left(b)
        if idx == len(cache):
            cache.append(b)
        else:
            cache[idx] = b

    return N - len(cache)

N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, wires))