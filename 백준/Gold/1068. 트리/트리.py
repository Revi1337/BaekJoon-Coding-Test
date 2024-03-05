import sys

input = sys.stdin.readline

def solution(n, tree, delete):

    DELETED = -100

    def delete_children(delete_node_idx):
        tree[delete_node_idx] = DELETED
        for child_node_idx in range(n):
            if delete_node_idx == tree[child_node_idx]:
                delete_children(child_node_idx)

    # Search And Delete Element Recursive
    delete_children(delete)

    # Count Leaf Node from Tree
    answer = 0
    for node_idx in range(n):
        if tree[node_idx] != DELETED and node_idx not in tree:
            answer += 1

    return answer
n = int(input())
tree = list(map(int, input().split()))
delete = int(input())
print(solution(n, tree, delete))
