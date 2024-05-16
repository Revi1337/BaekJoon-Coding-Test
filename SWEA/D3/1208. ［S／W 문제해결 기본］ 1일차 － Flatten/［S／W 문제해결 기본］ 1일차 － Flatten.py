def solution(seq, N, boxes):
    length = len(boxes)
    for _ in range(N):
        max_idx, max_num = 0, -1e9
        min_idx, min_num = 0, 1e9
        for idx in range(length):
            if boxes[idx] > max_num:
                max_idx, max_num = idx, boxes[idx]
            if boxes[idx] < min_num:
                min_idx, min_num = idx, boxes[idx]
        boxes[min_idx] += 1
        boxes[max_idx] -= 1
    return f'#{seq} {max(boxes) - min(boxes)}'

T = 10
for idx in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))
    print(solution(idx + 1, N, boxes))
