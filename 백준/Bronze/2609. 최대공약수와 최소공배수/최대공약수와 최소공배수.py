import sys

input = sys.stdin.readline

def solution(a, b):

    def gcd(a, b): # gcd 는 최대공약수를 의미 (유클리드 호제법)
        max_num, min_num = max(a, b), min(a, b)
        while max_num % min_num != 0:
            max_num, min_num = min_num, max_num % min_num
        return min_num

    def lcm(a, b, gcd): # lcm 은 최소공배수를 의미. a * b 를 gcd 의 결과로 나누면 된다.
        return (a * b) // gcd

    gcd_answer = gcd(a, b)
    lcm_answer = lcm(a, b, gcd_answer)

    print(gcd_answer)
    print(lcm_answer)


a, b = map(int, input().split())
solution(a, b)