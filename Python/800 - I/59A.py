s = input()
cnt1 = 0
cnt2 = 0
for i in s:
    cnt1 += i.islower()
    cnt2 += i.isupper()
print(s.lower() if cnt1>=cnt2 else s.upper())