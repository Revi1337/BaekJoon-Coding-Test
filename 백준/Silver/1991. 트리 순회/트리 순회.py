import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def solution(n, edges):
    graph = dict()
    for parent, child1, child2 in edges:
        graph[parent] = graph.get(parent, [])
        graph[parent].extend([child1, child2])

    def preorder(parent):
        child1, child2 = graph[parent]
        print(parent, end = '')
        if child1 != '.':
            preorder(child1)
        if child2 != '.':
            preorder(child2)

    def inorder(parent):
        child1, child2 = graph[parent]
        if child1 != '.':
            inorder(child1)
        print(parent, end = '')
        if child2 != '.':
            inorder(child2)

    def postorder(parent):
        child1, child2 = graph[parent]
        if child1 != '.':
            postorder(child1)
        if child2 != '.':
            postorder(child2)
        print(parent, end='')

    for function in [preorder, inorder, postorder]:
        function('A')
        if function != postorder:
            print()

n = int(input())
edges = [input().split() for _ in range(n)]
solution(n, edges)