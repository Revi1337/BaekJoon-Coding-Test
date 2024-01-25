def solution(hotel):
    for h, w, n in hotel:
        floor = n % h
        pos = (n // h) + 1
        if floor == 0:
            floor = h
            pos -= 1
        answer = f'{floor}{pos:0>2}'
        print(answer)

loop = int(input())
hotel = [list(map(int, input().split())) for _ in range(loop)]
solution(hotel)