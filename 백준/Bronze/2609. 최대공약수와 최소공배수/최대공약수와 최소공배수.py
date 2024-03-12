import sys

input = sys.stdin.readline
def solution(num1, num2):

    """ 최대공약수 """
    def gcd(num1, num2) -> int:
        min_num, max_num = min(num1, num2), max(num1, num2)
        while max_num % min_num > 0:
            max_num, min_num = min_num, max_num % min_num
        return min_num

    """ 최소공배수 """
    def lcm(num1, num2) -> int:
        return (num1 * num2) // gcd(num1, num2)

    gcd_num = gcd(num1, num2)
    lcm_num = lcm(num1, num2)

    print(gcd_num)
    print(lcm_num)

v1, v2 = map(int, input().split())
solution(v1, v2)