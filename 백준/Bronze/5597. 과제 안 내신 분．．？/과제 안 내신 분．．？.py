nums = [int(input()) for _ in range(28)]
pre = list(range(1,31))

answer = sorted(set(pre) - set(nums))
print(answer[0])
print(answer[1])