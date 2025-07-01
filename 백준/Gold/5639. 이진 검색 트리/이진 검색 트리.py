import sys

sys.setrecursionlimit(10 ** 5)

def solution(nodes):

    def recursive(nodes):
        if not len(nodes):
            return

        mid, left, right = nodes[0], [], []
        for n in range(1, len(nodes)):
            if mid < nodes[n]:
                left, right = nodes[1:n], nodes[n:]
                break
        else:
            left = nodes[1:]

        recursive(left)
        recursive(right)
        print(mid)

    recursive(nodes)


nodes = []
while True:
    try:
        node = int(input())
        nodes.append(node)
    except:
        break
solution(nodes)
