import math
n, m, z = map(int, input().split())
ans = n*m/math.gcd(n, m)
print(z/ans)


