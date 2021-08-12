x = int(input())
l, r = [], []
ans = 0
for i in range(x):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)
page = int(input())
for i in range(x):
    if l[i] <= page <= r[i]:
        ans = i
        break
print(x-ans)
