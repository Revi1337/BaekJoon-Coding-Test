def solution(string):
    chars = list(string)
    if chars.count(':') >= 8 and chars[0] == ':' == chars[1]:
        chars[0] = '0'
    elif chars.count(':') >= 8 and chars[-1] == ':' == chars[-2]:
        chars[-1] = '0'

    while chars.count(':') < 7:
        for idx in range(len(string) - 1):
            if chars[idx] == ':' == chars[idx + 1]:
                chars.insert(idx, ':')
                break

    fields = "".join(chars).split(':')
    answer = [f'{field:>04}' for field in fields]

    print(*answer, sep=':')

string = input().rstrip()
solution(string)