def solution(string):
    length = len(string)
    answer = [string[idx:] for idx in range(length - 1, -1, -1)]
    answer.sort()
    for char in answer:
        print(char)

solution(input())
