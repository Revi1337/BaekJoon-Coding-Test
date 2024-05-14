def solution(idx, N, datas):
    answer = ""
    cnt = 0
    for (char, counter) in datas:
        answer += (char * int(counter))
        cnt += int(counter)
    print(f'#{idx}')
    for i in range(0, cnt, 10):
        print(answer[i: i + 10])

T = int(input())
for idx in range(T):
    N = int(input())
    datas = [input().split() for _ in range(N)]
    solution(idx + 1, N, datas)
