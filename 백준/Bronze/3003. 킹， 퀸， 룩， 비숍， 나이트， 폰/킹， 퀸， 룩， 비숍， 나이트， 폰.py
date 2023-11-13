ches = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
for idx in range(6):
    print(ches[idx] - found[idx], end=" ")
