def solution(string):
    nums = list(map(int, string.split(' ')))
    mn, mx = min(nums), max(nums)
    return f'{mn} {mx}'