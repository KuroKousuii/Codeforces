def check(a):
    now, cnt = set(), 0
    while a:
        now.add(a%10)
        a //= 10
        cnt += 1
    return cnt == len(now)


down, up = map(int, input().split())
cur = -1
for i in range(down, up+1, 1):
    if check(i):
        cur = i
        break
print(cur)