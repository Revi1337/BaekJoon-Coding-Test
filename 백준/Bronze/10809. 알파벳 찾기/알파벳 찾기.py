from collections import defaultdict
import string

lowercase = string.ascii_lowercase
answer = [-1] * len(lowercase)
strings = input()
counter = defaultdict(int)

for idx in range(len(strings)):
    if strings[idx] not in counter:
        counter[strings[idx]] = idx

for idx in range(len(lowercase)):
    for hash in counter:
        if lowercase[idx] == hash:
            answer[idx] = counter[hash]

print(*answer)
