x = int(input())
cnt1, cnt2 = 0, 0
for _ in range(x):
    a, b = map(int, input().split())
    cnt1 += a == 1
    cnt2 += b == 1
print(min(cnt1, x-cnt1)+min(cnt2, x-cnt2))