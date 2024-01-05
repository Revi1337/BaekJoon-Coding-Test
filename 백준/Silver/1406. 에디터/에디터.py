import sys

# 스택을 두개 사용하여 해결
def solution(string, operations):
    stack1 = list(string)
    stack2 = []
    for operation in operations:
        if operation[0] == 'L' and stack1:
            stack2.append(stack1.pop())
        elif operation[0] == 'D' and stack2:
            stack1.append(stack2.pop())
        elif operation[0] == 'B' and stack1:
            stack1.pop()
        elif operation[0] == 'P':
            stack1.append(operation[1])
    return "".join(stack1 + list(reversed(stack2)))

string = sys.stdin.readline().rstrip()
loop = int(sys.stdin.readline())
operations = [sys.stdin.readline().rstrip().split() for _ in range(loop)]
print(solution(string, operations))
