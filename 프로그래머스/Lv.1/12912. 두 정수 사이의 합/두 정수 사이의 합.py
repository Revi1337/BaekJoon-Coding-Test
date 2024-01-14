def solution(a, b):
    if a == b:
        return a
    else:
        return sum([val for val in range(min(a,b), max(a,b) + 1)])