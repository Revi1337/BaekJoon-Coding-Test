def solution(seq, N):
    nums = {num: 0 for num in [2,3,5,7,11]}
    for num in nums:
        while True:
            if not N % num:
                nums[num] += 1
                N /= num
            else:
                break
    print(f'#{seq} {" ".join(map(str, nums.values()))}')

T = int(input())
for idx in range(T):
    N = int(input())
    solution(idx + 1, N)