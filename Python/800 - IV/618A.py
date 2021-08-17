ok = False
for _ in range(int(input())):
    s, a, b = input().split()
    if int(b) > int(a) > 2399:
        ok = True
print("YES" if ok else "NO")