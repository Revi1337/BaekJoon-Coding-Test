def solution(string):
    p, m = 31, 1234567891
    answer = 0
    for idx, char in enumerate(string):
        value = ord(char) - 97 + 1
        answer += value * pow(p, idx)
    answer %= m
    return answer

_ = int(input())
string = input()
print(solution(string))