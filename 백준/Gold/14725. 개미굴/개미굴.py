def solution(N, edges):

    def put(dic, nodes):
        if not len(nodes):
            return

        if nodes[0] not in dic:
            dic[nodes[0]] = {}
        put(dic[nodes[0]], nodes[1:])

    def prt(dic, level):
        for node in sorted(dic):
            print('--' * level + node)
            prt(dic[node], level + 1)

    dic = {}
    for edge in edges:
        put(dic, edge[1:])
    prt(dic, 0)

N = int(input())
edges = [list(input().rstrip().split()) for _ in range(N)]
solution(N, edges)
