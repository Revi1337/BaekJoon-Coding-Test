res = []
while True:
    val = input()
    if val == '#':
        break
    cnt = 0
    for i in val:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1
    res.append(cnt)
for i in res: print(i)



            
    