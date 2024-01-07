def solution(data):
    delemiter = len(data) // 2
    return int("".join(map(str, data[:delemiter]))) + int("".join(map(str, data[delemiter:])))

print(solution(list(map(int, input().split()))))

