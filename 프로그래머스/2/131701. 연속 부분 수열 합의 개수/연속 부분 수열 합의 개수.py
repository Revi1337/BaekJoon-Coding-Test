def solution(elements):
    n = len(elements)
    elements = elements * 2
    psum = [0] * (len(elements) + 1)
    for idx in range(1, len(psum)):
        psum[idx] = psum[idx - 1] + elements[idx - 1]

    cache = set()
    for length in range(1, n + 1):
        for start in range(n):
            total = psum[start + length] - psum[start]
            cache.add(total)

    return len(cache)