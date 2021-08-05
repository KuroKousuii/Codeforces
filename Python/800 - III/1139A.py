x, ans = int(input()), 0
s = input()
for i in range(x):
    ans += (ord(s[i]) % 2 == 0)*(i+1)
print(ans)

