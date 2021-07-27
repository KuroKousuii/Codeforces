x = int(input())
s1 = input()
s2 = input()
total = 0
for i in range(x):
    check = min(abs(ord(s1[i])-ord(s2[i])), 10-abs(ord(s1[i])-ord(s2[i])))
    total += check
print(total)
