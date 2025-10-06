def solution(m, musicinfos):

    def convert(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    def convert_lst(melody):
        st, mel = 0, []
        while st < len(melody):
            tmp = melody[st:st + 2]
            if len(tmp) == 2 and tmp[1] == '#':
                mel.append(tmp)
                st += 2
            else:
                mel.append(melody[st])
                st += 1
        return mel

    m = convert_lst(m)
    musics = []
    for line in musicinfos:
        st, end, name, mus = line.split(',')
        mus = convert_lst(mus)
        time = convert(end) - convert(st)
        while len(mus) < time:
            mus.extend(mus)
        musics.append([convert(end) - convert(st), mus[:time], name])

    ans = []
    for entry in musics:
        idxes = []
        for idx in range(len(entry[1])):
            if entry[1][idx] == m[0]:
                idxes.append(idx)
        for idx in idxes:
            if entry[1][idx:idx + len(m)] == m:
                ans.append([*entry])
                break

    ans.sort(key=lambda x: (-x[0]))
    if not ans:
        return '(None)'
    return ans[0][2]