a, b = map(int, input().split())
cnt = 1
while (cnt*a) % 10 and (cnt*a) % 10 != b:
    cnt += 1
print(cnt)