def solution(number, limit, power):
    divisors = []
    for num in range(1, number + 1):
        divisor = 0
        for integer in range(1, int(num **(1/2)) + 1):
            if num % integer == 0:
                divisor += 1
                if integer ** 2 != num:  # 제곱이 되는 수는 count 1을 하여 중복 방지.
                    divisor += 1
            if divisor > limit:  # limit값을 초과하면 power값으로 return
                divisor = power
                break
        divisors.append(divisor)
    return sum(divisors)