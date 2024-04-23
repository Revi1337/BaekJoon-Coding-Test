import sys

input = sys.stdin.readline

def solution(K, directions):
    dir_arr = [[] for _ in range(5)]
    for direction in directions:
        dir_arr[direction[0]].append(direction[1])

    size = 1
    for idx in range(1, 5):
        if len(dir_arr[idx]) == 1:
            size *= dir_arr[idx][0]

    sub_size = 1
    for idx in range(6):
        if directions[(idx - 1) % 6][0] == directions[(idx + 1) % 6][0]:
            sub_size *= directions[idx][1]
            
    return (size - sub_size) * K

K = int(input().rstrip())
directions = [list(map(int, input().split())) for _ in range(6)]
print(solution(K, directions))
