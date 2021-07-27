s = input()
cnt = 0
for i in s:
    cnt += i == '4' or i == '7'
print("YES" if cnt == 4 or cnt == 7 else "NO")