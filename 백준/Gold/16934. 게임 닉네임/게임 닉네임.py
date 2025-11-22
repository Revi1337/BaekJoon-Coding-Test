# 2025-11-22
# https://www.acmicpc.net/problem/16934

import sys

input = sys.stdin.readline

def solution(N, S):

    def insert(trie, word):
        pfx = ""
        for char in word:
            pfx += char
            if char not in trie:
                trie[char] = {}
                trie = trie[char]
                for rchar in word[len(pfx):]:
                    trie[rchar] = {}
                    trie = trie[rchar]
                return pfx
            trie = trie[char]

        return word if counter[word] == 1 else word + str(counter[word])

    trie, counter, ans = {}, {}, []
    for name in S:
        counter[name] = counter.get(name, 0) + 1
        alias = insert(trie, name)
        ans.append(alias)

    print(*ans, sep='\n')

N = int(input())
S = [input().rstrip() for _ in range(N)]
solution(N, S)
