def solution(string):
    pri = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    oper, postfix = [], []

    for char in string:
        if 'A' <= char <= 'Z':
            postfix.append(char)
        elif char == '(':
            oper.append(char)
        elif char == ')':
            while oper and oper[-1] != '(':
                postfix.append(oper.pop())
            oper.pop()
        else:
            while oper and pri[char] <= pri[oper[-1]]:
                postfix.append(oper.pop())
            oper.append(char)

    while oper:
        postfix.append(oper.pop())

    return ''.join(postfix)

string = input().rstrip()
print(solution(string))
