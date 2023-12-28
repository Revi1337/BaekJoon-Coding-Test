def solution(nums):
    nums.sort(key=lambda x: (x[0], x[1]))
    for num in nums:
        print(num[0], num[1])

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
solution(arr)
