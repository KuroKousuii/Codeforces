x, y = map(int, input().split())
ok = False
for i in range(x):
    s = input()
    if s.find('Y') != -1 or s.find('M') != -1 or s.find('C') != -1:
        ok = True
print("#Color" if ok else "#Black&White")
