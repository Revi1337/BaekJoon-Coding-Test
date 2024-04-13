import sys

input = sys.stdin.readline

def solution(trees):
    length = len(trees)
    tree_dict = {}
    for tree in trees:
        tree_dict[tree] = tree_dict.get(tree, 0) + 1

    sorted_trees = sorted(tree_dict.keys())
    for tree in sorted_trees:
        frequency = tree_dict[tree]
        frequency = (frequency / length * 100)
        print("%s %.4f" % (tree, frequency))

trees = []
while True:
    tree = input().rstrip()
    if tree == '':
        break
    trees.append(tree)

solution(trees)

