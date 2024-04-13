import sys

input = sys.stdin.readline

def solution(n, logs):
    log_dict = {}
    for (name, status) in logs:
        if status == 'enter':
            value = 1
        elif status == 'leave':
            value = -1
        log_dict[name] = log_dict.get(name, 0) + value

    answer = sorted(
        map(
            lambda x: x[0],
            filter(
                lambda x: x[1] != 0,
                log_dict.items()
            )
        ),
        reverse=True
    )

    for ans in answer:
        print(ans)

n = int(input().rstrip())
logs = [input().split() for _ in range(n)]
solution(n, logs)
