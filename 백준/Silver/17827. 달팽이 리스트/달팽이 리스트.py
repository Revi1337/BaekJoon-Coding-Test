import sys

input = sys.stdin.readline

def solution(N, M, V, seq, questions):
    V -= 1
    for q in questions:
        if q <= N - 1:
            print(seq[q])
        else:
            new = seq[V:]
            nlen = N - V
            print(new[(q - V) % nlen])

N, M, V = map(int, input().split())
seq = list(map(int, input().split()))
questions = [int(input()) for _ in range(M)]
solution(N, M, V, seq, questions)