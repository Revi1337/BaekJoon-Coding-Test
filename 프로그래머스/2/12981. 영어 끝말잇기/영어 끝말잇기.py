def solution(n, words):
    length = len(words)
    storage = set()
    storage.add(words[0])
    last_char = words[0][-1]
    for idx in range(1, length):
        word = words[idx]
        first_char = word[0]
        if (first_char != last_char) or (word in storage):
            pre = (idx // n) * n
            result = idx - pre
            return [result + 1, (idx // n) + 1]
        storage.add(word)
        last_char = word[-1]
    return [0, 0]