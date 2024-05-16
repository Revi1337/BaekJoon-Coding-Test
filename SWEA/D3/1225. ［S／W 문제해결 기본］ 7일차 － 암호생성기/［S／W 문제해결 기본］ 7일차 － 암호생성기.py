def solution(seq, integers):
    offset = 1
    while True:
        if offset > 5:
            offset = 1
        t = integers.pop(0) - offset
        if t <= 0:
            integers.append(0)
            break
        integers.append(t)
        offset += 1

    print(f'#{seq}', end = ' ')
    print(*integers)

T = 10
for _ in range(T):
    seq = int(input())
    integers = list(map(int, input().rstrip().split()))
    solution(seq, integers)