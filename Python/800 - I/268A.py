home, oppo = [], []
x = int(input())
cnt = 0
for i in range(x):
    cur1, cur2 = map(int, input().split())
    home.append(cur1)
    oppo.append(cur2)
for i in home:
    for j in oppo:
        cnt += i == j
print(cnt)