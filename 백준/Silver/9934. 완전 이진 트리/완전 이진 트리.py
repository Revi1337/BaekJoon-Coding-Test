def solution(K, B):

    def recursive(lst, lv):
        half = len(lst) // 2
        left, right = lst[:half], lst[half + 1:]
        lvs[lv].append(lst[half])
        if left:
            recursive(left, lv + 1)
        if right:
            recursive(right, lv + 1)

    lv = cnt = 0
    while cnt < len(B):
        lv += 1
        cnt += 2 ** (lv - 1)
    lvs = [[] for _ in range(lv)]
    recursive(B, 0)

    for lv in lvs:
        print(*lv)

K = int(input())
B = list(map(int, input().split()))
solution(K, B)