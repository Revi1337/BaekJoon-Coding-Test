def solution(seq, target):
    answer = 0
    length = len(target)
    original = "0" * length
    for idx in range(length):
        if original[idx] != target[idx]:
            if target[idx] == '1':
                original = original[:idx] + ('1' * (length - idx))
            else:
                original = original[:idx] + ('0' * (length - idx))
            answer += 1
    return f'#{seq} {answer}'

T = int(input())
for seq in range(T):
    target = input().rstrip()
    print(solution(seq + 1, target))
