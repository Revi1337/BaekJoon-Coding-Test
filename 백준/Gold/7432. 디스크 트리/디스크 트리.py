# 2025-11-21
# https://www.acmicpc.net/problem/7432

import sys

input = sys.stdin.readline

def solution(N, P):

    def insert(trie, paths):
        for dir in paths:
            if dir not in trie:
                trie[dir] = {}
            trie = trie[dir]

    def logging(trie, pad):
        trie = {key: trie[key] for key in sorted(trie.keys())}
        for dir in trie:
            print(' ' * pad + dir)
            logging(trie[dir], pad + 1)

    P = [path.split('\\') for path in P]
    trie = {}
    for path in P:
        insert(trie, path)
    logging(trie, 0)

N = int(input())
P = [input().rstrip() for _ in range(N)]
solution(N, P)
