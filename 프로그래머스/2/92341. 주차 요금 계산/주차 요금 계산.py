def solution(fees, records):
    DAY = 60 * 23 + 59

    dic = {}
    for record in records:
        time, num, type = record.split()
        dic[num] = dic.get(num, [])
        hour, mi = time.split(':')
        dic[num].append([int(hour) * 60 + int(mi), type])

    keys = sorted(dic)
    sums = []
    for key in keys:
        stack = []
        sm = 0
        for entry in dic[key]:
            if not stack or entry[1] == 'IN':
                stack.append(entry)
                continue

            if entry[1] == 'OUT' and stack[-1][1] == 'IN':
                in_time, _ = stack.pop()
                out_time = entry[0]
                sm += out_time - in_time
        for time, _ in stack:
            sm += DAY - time
        sums.append(sm)

    ans = []
    for sm in sums:
        if sm <= fees[0]:
            ans.append(fees[1])
        else:
            overflow = sm - fees[0]
            if overflow % fees[2]:
                ans.append(fees[1] + ((overflow // fees[2]) + 1) * fees[3])
            else:
                ans.append(fees[1] + (overflow // fees[2]) * fees[3])

    return ans