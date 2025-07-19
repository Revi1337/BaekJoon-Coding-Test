def solution(N, Q, LO, QU):

    def yoon(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def convert(date, time):
        Y, M, D = map(int, date.split('-'))
        h, m, s = map(int, time.split(':'))
        sec = 0
        sec += s
        sec += m * 60
        sec += h * 60 * 60
        sec += (D - 1) * 24 * 60 * 60

        for y in range(2000, Y):
            if yoon(y):
                sec += 366 * 24 * 60 * 60
            else:
                sec += 365 * 24 * 60 * 60

        md = [31, 28 + bool(yoon(Y)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(M - 1):
            sec += md[m] * 24 * 60 * 60

        return sec

    def lower_bound(t):
        left, right = 0, len(logs)
        while left < right:
            mid = (left + right) // 2
            if logs[mid] < t:
                left = mid + 1
            else:
                right = mid

        return right

    def upper_bound(t):
        left, right = 0, len(logs)
        while left < right:
            mid = (left + right) // 2
            if logs[mid] <= t:
                left = mid + 1
            else:
                right = mid

        return right

    logs, lvs = [[] for _ in range(2)]
    for log in LO:
        datetime, lv = log.split('#')
        sec, lv = convert(*datetime.split()), int(lv)
        logs.append(sec)
        lvs.append(lv)

    lsum = [0] * (N + 1)
    lsum[0] = [0] * 7
    for idx in range(1, N + 1):
        lsum[idx] = [*lsum[idx - 1]]
        lsum[idx][lvs[idx - 1]] += 1

    logs.sort()
    for q in QU:
        t1, t2, lv = q.split('#')
        sec1, sec2, lv = convert(*t1.split()), convert(*t2.split()), int(lv)
        idx1, idx2 = lower_bound(sec1), upper_bound(sec2)
        print(sum(lsum[idx2][l] - lsum[idx1][l] for l in range(lv, 7)))


N, Q = map(int, input().split())
LO = [input().rstrip() for _ in range(N)]
QU = [input().rstrip() for _ in range(Q)]
solution(N, Q, LO, QU)