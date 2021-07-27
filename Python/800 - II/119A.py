import math
a, b, n = map(int, input().split())
ok = True
while n != 0:
    if ok:
        n -= math.gcd(a, n)
    else:
        n -= math.gcd(b, n)
    ok = not ok
print(1 if ok else 0)
