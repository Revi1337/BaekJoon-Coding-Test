def solution(string: str):
    rev = string[::-1]
    return 1 if string == rev else 0

print(solution(input()))
