import sys

input = sys.stdin.readline

A, B = map(int, input().split())
pre1 = int(bin(A), 2) + int(bin(B), 2)
print(pre1)
