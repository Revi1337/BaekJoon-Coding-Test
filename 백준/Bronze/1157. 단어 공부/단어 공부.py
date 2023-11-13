from collections import defaultdict

def solution(data):
    counter = defaultdict(int)
    for val in data:
        counter[val.lower()] += 1
    max = None
    max_count = 0
    for hash in counter:
        if counter[hash] > max_count:
            max = hash
            max_count = counter[hash]
    cnt = 0
    for hash in counter:
        if counter[hash] == max_count:
            cnt += 1
        if cnt == 2:
            return "?"
    return max.upper()

print(solution(input()))