# 2026-04-25
# https://www.acmicpc.net/problem/14725
# 개미굴
# tree
# trie

import sys

input = sys.stdin.readline

def solution(N, E):

    def insert(words, trie):
        for word in words:
            if word not in trie:
                trie[word] = {}
            trie = trie[word]

    def dfs(word, trie, d):
        if word:
            print(f"{'--' * d}{word}")
        for word in trie:
            dfs(word, trie[word], d + 1)

    E = [entry[1:] for entry in E]
    E.sort()

    trie = {}
    for words in E: insert(words, trie)

    dfs('', trie, -1)

N = int(input())
E = [list(input().rstrip().split()) for _ in range(N)]
solution(N, E)
