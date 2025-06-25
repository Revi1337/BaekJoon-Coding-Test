def solution(string, deli):
    deli = deli[::-1]
    length = len(deli)
    curr, stack = length, []

    for char in string:
        stack.append(char)
        if len(stack) >= length and "".join(stack[-1:-length-1:-1]) == deli:
            for _ in range(length):
                stack.pop()

    return "".join(stack) if stack else "FRULA"

string = input().rstrip()
deli = input().rstrip()
print(solution(string, deli))