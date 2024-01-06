import sys

def solution(word):
    stack = []
    answer = ""
    tag = False
    for char in word:
        if char == '<':
            answer += "".join(reversed(stack))
            stack.clear()
            stack.append(char)
            tag = True
            continue
        elif char == '>':
            stack.append(char)
            answer += "".join(stack)
            stack.clear()
            tag = False
            continue

        if tag:
            stack.append(char)
        else:
            if char == ' ':
                answer += "".join(reversed(stack)) + ' '
                stack.clear()
            else:
                stack.append(char)
    answer += "".join(reversed(stack))

    return answer

word = sys.stdin.readline().rstrip()
print(solution(word))
