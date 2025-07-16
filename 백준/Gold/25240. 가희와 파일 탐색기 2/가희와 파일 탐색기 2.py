mapper = {'X': 1, 'W': 2, 'R': 4}

def solution(U, F, US, FI, Q, QU):
    files, groups = [{} for _ in range(2)]
    for entry in US:
        u, *g = entry.split()
        groups[u] = groups.get(u, set())
        groups[u].add(u)
        if g:
            for g in g[0].split(','):
                groups[g] = groups.get(g, set())
                groups[g].add(u)

    for name, perm, owner, group in FI:
        files[name] = files.get(name, [])
        files[name].extend([int(perm[0]), int(perm[1]), int(perm[2]), owner, group])

    for user, file, per in QU:
        per = mapper[per]
        up, gp, op, ow, gr = files[file]
        if user == ow and up & per == per:
            print(1)
            continue
        if (user == gr and gp & per == per) or (user in groups[gr] and gp & per == per):
            print(1)
            continue
        if op & per == per:
            print(1)
            continue

        print(0)

U, F = map(int, input().split())
US = [input().rstrip() for _ in range(U)]
FI = [input().rstrip().split() for _ in range(F)]
Q = int(input())
QU = [input().rstrip().split() for _ in range(Q)]
solution(U, F, US, FI, Q, QU)