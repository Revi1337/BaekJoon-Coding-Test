def solution(string):
    answer = ""
    stack = []
    for char in string:
        if char == ' ':
            answer += (''.join(stack[::-1]) + ' ')
            stack.clear()
        else:
            stack.append(char)
    answer += ''.join(stack[::-1])
    print(answer)

loop = int(input())
for _ in range(loop):
    solution(input())