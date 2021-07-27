import math


def check(a):
    x, total = a, 0
    while x:
        total += x % 10
        x //= 10
    return math.gcd(total, a) > 1


for _ in range(int(input())):
    n = int(input())
    while not check(n):
        n += 1
    print(n)