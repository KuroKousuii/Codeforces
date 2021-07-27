import math
x, y = map(int, input().split())
check = 7-max(x, y)
print(f'{check//math.gcd(check,6)}/{6//math.gcd(check, 6)}')
