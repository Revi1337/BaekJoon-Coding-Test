from collections import deque

def solution(begin, target, words):
    length = len(begin)
    check, words = {begin}, set(words)
    queue = deque([[list(begin), 0]])
    while queue:
        chars, cnt = queue.popleft()
        if "".join(chars) == target:
            return cnt
        for idx in range(length):
            init = chars[idx]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == chars[idx]:
                    continue
                chars[idx] = c
                word = "".join(chars)
                if word in words and word not in check:
                    queue.append([[*chars], cnt + 1])
                    check.add(word)
            chars[idx] = init

    return 0
