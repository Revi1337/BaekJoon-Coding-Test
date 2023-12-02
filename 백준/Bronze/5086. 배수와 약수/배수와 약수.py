def solution(one, two):
    if two % one == 0:
        return 'factor'
    elif one % two == 0:
        return 'multiple'
    else:
        return 'neither'

while True:
    one, two = map(int, input().split())
    if one == 0 and two == 0:
        break
    print(solution(one, two))

