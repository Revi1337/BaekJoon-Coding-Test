def solution(string):
    length = len(string)
    answer = [string[idx:] for idx in range(length)]
    answer.sort()
    for char in answer:
        print(char)

solution(input())
