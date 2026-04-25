# 2026-04-25
# https://www.acmicpc.net/problem/5052
# 전화번호 목록
# trie

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

    W.sort()
    trie = {}
    for word in W:
        if can_insert(word, trie):
            insert(word, trie)
        else:
            return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    N = int(input())
    W = [input().rstrip() for _ in range(N)]
    print(solution(N, W))
