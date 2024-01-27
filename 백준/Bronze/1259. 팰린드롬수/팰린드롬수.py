while True:
    string = input()
    if string == '0':
        break
    answer = ''
    length = len(string)
    for idx in range(length - 1, -1, -1):
        answer += string[idx]
    if string == answer:
        print('yes')
    else:
        print('no')
