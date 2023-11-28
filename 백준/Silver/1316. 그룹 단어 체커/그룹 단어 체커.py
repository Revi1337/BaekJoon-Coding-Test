answer = [0]
def solution(string: str):
    cache = ''
    if len(string) == 1:
        answer[0] += 1
        return
    for idx in range(1, len(string)):
        if string[idx] in cache:
            return
        if string[idx - 1] != string[idx]:
            cache += string[idx - 1]
    answer[0] += 1

loop = int(input())
for _ in range(loop):
    solution(input())
print(answer[0])
