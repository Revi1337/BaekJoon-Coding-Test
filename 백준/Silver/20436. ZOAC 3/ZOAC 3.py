import sys

input = sys.stdin.readline

keyboard = {
    'q': [0, 0],
    'w': [0, 1],
    'e': [0, 2],
    'r': [0, 3],
    't': [0, 4],
    'y': [0, 5],
    'u': [0, 6],
    'i': [0, 7],
    'o': [0, 8],
    'p': [0, 9],

    'a': [1, 0],
    's': [1, 1],
    'd': [1, 2],
    'f': [1, 3],
    'g': [1, 4],
    'h': [1, 5],
    'j': [1, 6],
    'k': [1, 7],
    'l': [1, 8],

    'z': [2, 0],
    'x': [2, 1],
    'c': [2, 2],
    'v': [2, 3],
    'b': [2, 4],
    'n': [2, 5],
    'm': [2, 6]
}

def solution(l, r, string):
    zaum = {'r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g'}
    moum = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm'}
    left, right = [*keyboard[l]], [*keyboard[r]]
    answer = 0
    for char in string:
        if char in zaum:
            lr, lc = keyboard[char]
            distance = abs(left[0] - lr) + abs(left[1] - lc)
            answer += distance
            answer += 1
            left = [lr, lc]
        elif char in moum:
            rr, rc = keyboard[char]
            distance = abs(right[0] - rr) + abs(right[1] - rc)
            answer += distance
            answer += 1
            right = [rr, rc]
    return answer

l, r = input().strip().split()
string = input().strip()
print(solution(l, r, string))

