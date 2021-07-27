m, n = map(int, input().split())
cnt = 0
for i in range(m+1):
    for j in range(n+1):
        cnt += i*i+j == m and i+j*j == n
print(cnt)
