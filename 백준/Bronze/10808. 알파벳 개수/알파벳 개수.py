import sys

seed = "abcdefghijklmnopqrstuvwxyz"

def solution(data):
    answer = [0] * len(seed)
    for val in data:
        answer[ord(val) - 97] += 1      # 현재 단어의 ASII 코드에서 소문자 a 의 ASCII 코드를 뺀 값을 idx 로 사용
    for char in answer:
        print(char, end = ' ')


data = sys.stdin.readline().rstrip()
solution(data)
