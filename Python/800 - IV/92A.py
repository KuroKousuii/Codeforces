n, m = map(int, input().split())
m %= (n+1)*n//2
start = 1
while m - start >= 0:
    m -= start
    start += 1
print(m)