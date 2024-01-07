import sys

seed = "abcdefghijklmnopqrstuvwxyz"

def solution(data):
    answer = [0] * len(seed)
    for idx in range(len(seed)):
        for val in data:
            if seed[idx] == val:
                answer[idx] += 1
    return " ".join(map(lambda x: str(x), answer))


data = sys.stdin.readline().rstrip()
print(solution(data))
