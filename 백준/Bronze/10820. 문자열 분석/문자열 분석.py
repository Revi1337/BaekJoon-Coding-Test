def solution(data):
    answer = [0] * 4
    for char in data:
        if 65 <= ord(char) <= 90:
            answer[1] += 1
        elif 97 <= ord(char) <= 122:
            answer[0] += 1
        elif char == ' ':
            answer[3] += 1
        else:
            answer[2] += 1

    for char in answer:
        print(char, end = ' ')
    print()

while True:
    try:
        solution(input())
    except Exception as e:
        break