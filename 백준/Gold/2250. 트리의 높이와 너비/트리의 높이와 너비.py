def solution(node_cnt, edges):
    level_row = [[] for _ in range(node_cnt + 1)]
    col = 1

    def init_graph_and_rootnode():
        node_metadata = [0] * (node_cnt + 1)
        graph = [0] * (node_cnt + 1)
        for curr_node, child1, child2 in edges:
            node_metadata[curr_node] += 1
            if child1 != -1:
                node_metadata[child1] += 1
            if child2 != -1:
                node_metadata[child2] += 1
            graph[curr_node] = [child1, child2]

        return graph, node_metadata.index(1)

    def dfs(node, level):
        nonlocal col
        left, right = graph[node]
        if graph[node][0] != -1:
            dfs(left, level + 1)
        level_row[level].append(col)
        col += 1
        if graph[node][1] != -1:
            dfs(right, level + 1)

    graph, rootnode = init_graph_and_rootnode()
    dfs(rootnode, 1)

    max_level, max_width = 1, max(level_row[1]) - min(level_row[1]) + 1
    for level, rows in enumerate(level_row[1:], start=1):
        if len(rows) >= 2:
            width = max(rows) - min(rows) + 1
            if width > max_width:
                max_level, max_width = level, width

    print(max_level, max_width)

node_cnt = int(input())
edges = [list(map(int, input().split())) for _ in range(node_cnt)]
solution(node_cnt, edges)
