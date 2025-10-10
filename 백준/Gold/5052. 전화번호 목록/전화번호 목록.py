def solution(N, W):

    def can_insert(word, trie):
        for char in word:
            if char not in trie:
                return True
            if not trie[char]:
                return False
            trie = trie[char]
        return True

    def insert(word, trie):
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

    W.sort(key=lambda x: len(x))
    trie = {}
    for word in W:
        if not can_insert(word, trie):
            return 'NO'
        insert(word, trie)
    return 'YES'

T = int(input())
for _ in range(T):
    N = int(input())
    W = [input().rstrip() for _ in range(N)]
    print(solution(N, W))