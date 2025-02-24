def solution(string):

    def recursive(parts, fb, bidx):
        if not parts:
            return

        mchar = min(parts)
        midx = parts.index(mchar)
        if fb == 'b':
            answer.insert(bidx + 1, mchar)
            nidx = bidx + 1
        elif fb == 'f':
            answer.insert(bidx, mchar)
            nidx = bidx

        print(*answer, sep = '')

        recursive(parts[midx + 1:], 'b', nidx)
        recursive(parts[:midx], 'f', nidx)

    answer = []
    recursive(string, 'f', 0)

string = input().rstrip()
solution(string)