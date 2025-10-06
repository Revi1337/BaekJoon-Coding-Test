def solution(files):
    lfiles = []
    for name in files:
        nidx, tidx = None, len(name)
        for idx in range(len(name)):
            if name[idx].isdecimal():
                nidx = idx
                break

        for idx in range(nidx + 1, len(name)):
            if not name[idx].isdecimal() and name[idx - 1].isdecimal():
                tidx = idx
                break
        lfiles.append([name[:nidx].lower(), int(name[nidx:tidx]), name[tidx:].lower(), name])


    lfiles.sort(key = lambda x: (x[0], x[1]))
    return [file[3] for file in lfiles]