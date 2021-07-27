x = int(input())
s = input()
cnt1, cnt2 = 0, 0
for i in range(x-1):
    cnt1 += s[i+1] == 'F' and s[i] == 'S'
    cnt2 += s[i+1] == 'S' and s[i] == 'F'
print("YES" if cnt2 < cnt1 else "NO")