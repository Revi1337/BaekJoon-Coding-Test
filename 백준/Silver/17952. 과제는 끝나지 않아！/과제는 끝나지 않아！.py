import sys

input = sys.stdin.readline

def solution(N, datas):
    datas.insert(0, [0])
    memory = []
    counter = 1
    answer = 0
    while counter <= N:
        length = len(datas[counter])
        if length > 1:
            datas[counter][2] -= 1
            if datas[counter][2] == 0:
                answer += datas[counter][1]
            else:
                memory.append(datas[counter])
        else:
            if memory:
                memory[-1][2] -= 1
                if memory[-1][2] == 0:
                    answer += memory[-1][1]
                    memory.pop()
        counter += 1

    return answer

N = int(input())
datas = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, datas))