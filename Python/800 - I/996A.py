n = int(input())
cnt = 0
while n >= 100:
    n -= 100
    cnt += 1
while n >= 20:
    n -= 20
    cnt += 1
while n >= 10:
    n -= 10
    cnt += 1
while n >= 5:
    n -= 5
    cnt += 1
while n >= 1:
    n -= 1
    cnt += 1
print(cnt)