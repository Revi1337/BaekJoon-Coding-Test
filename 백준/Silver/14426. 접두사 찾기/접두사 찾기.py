def solution(N, M, W, T):

    def insert(trie, word):
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

    def starts_with(trie, prefix):
        idx = 0
        while idx < len(prefix):
            if prefix[idx] in trie:
                trie = trie[prefix[idx]]
            else:
                return
            idx += 1
        else:
            nonlocal answer
            answer += 1

    trie = {}
    for word in W:
        insert(trie, word)

    answer = 0
    for prefix in T:
        starts_with(trie, prefix)

    return answer


N, M = map(int, input().split())
W = [input().rstrip() for _ in range(N)]
T = [input().rstrip() for _ in range(M)]
print(solution(N, M, W, T))