def solution(T, string):
    for length in range(1, 11):
        if string[:length] == string[length: length * 2]:
            return f'#{T} {len(string[:length])}'

T = int(input())
for idx in range(T):
    string = input().rstrip()
    print(solution(idx + 1, string))