def solution(S, P, string, code):
    chars = list(string)
    psum = [0] * (S + 1)
    psum[0] = [0] * 26
    for idx in range(1, S + 1):
        psum[idx] = [*psum[idx - 1]]
        psum[idx][ord(chars[idx - 1]) - 65] += 1

    ans = 0
    for idx in range(P, S + 1):
        if psum[idx][ord('A') - 65] - psum[idx - P][ord('A') - 65] < code[0]:
            continue
        if psum[idx][ord('C') - 65] - psum[idx - P][ord('C') - 65] < code[1]:
            continue
        if psum[idx][ord('G') - 65] - psum[idx - P][ord('G') - 65] < code[2]:
            continue
        if psum[idx][ord('T') - 65] - psum[idx - P][ord('T') - 65] < code[3]:
            continue
        ans += 1

    return ans

S, P = map(int, input().split())
string = input().rstrip()
code = list(map(int, input().split()))
print(solution(S, P, string, code))
