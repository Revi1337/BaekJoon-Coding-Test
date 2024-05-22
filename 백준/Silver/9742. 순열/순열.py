import sys

input = sys.stdin.readline

def solution(string, find):
    string = str(string)
    length = 1
    for num in range(1, len(string) + 1):
        length *= num
    if length < int(find):
        return f'{string} {find} = No permutation'

    counter = 0
    def solve(characters, i):
        if i == len(string):
            nonlocal counter
            counter += 1
            if counter == int(find):
                return characters
        else:
            for k in string:
                if k not in characters:
                    res = solve(characters + k, i + 1)
                    if res:
                        return res

    answer = solve('', 0)
    return f'{string} {find} = {answer}'

while True:
    value = input()
    if value == '':
        break
    string, find = value.split()
    print(solution(string, find))
