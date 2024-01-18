from collections import Counter

def solution(nums):
    length = len(nums)
    choice = length // 2
    counter = Counter(nums)
    kind = sorted(counter.values())
    return min(choice, len(kind))