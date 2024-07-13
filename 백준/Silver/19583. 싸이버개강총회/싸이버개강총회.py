import sys

input = sys.stdin.readline

def solution(S, E, Q, datas):

    def convert_time(time):
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute

    ddict = {}
    for data in datas:
        time, nickname = data.split()
        ttime = convert_time(time)
        ddict[ttime] = ddict.get(ttime, set())
        ddict[ttime].add(nickname)

    part_users = set()
    end_users = set()
    st_time = convert_time(S)
    end_time = convert_time(E)
    send_time = convert_time(Q)

    for time in ddict:
        if time <= st_time:
            part_users = part_users | ddict[time]
        if end_time <= time <= send_time:
            end_users = end_users | ddict[time]

    answer = 0
    for user in end_users:
        if user in part_users:
            answer += 1

    return answer

S, E, Q = input().split()
datas = []
while True:
    data = input().strip()
    if data == '':
        print(solution(S, E, Q, datas))
        break
    datas.append(data)
