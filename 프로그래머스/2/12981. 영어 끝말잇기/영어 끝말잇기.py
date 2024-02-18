def solution(k, words):
    previous_word = words[0]
    duplicate = {previous_word}
    for idx, current_word in enumerate(words[1:], start=1):
        if (current_word[0] != previous_word[-1]) or (current_word in duplicate):
            return [(idx % k) + 1, (idx // k) + 1]
        duplicate.add(current_word)
        previous_word = current_word
    return [0, 0]