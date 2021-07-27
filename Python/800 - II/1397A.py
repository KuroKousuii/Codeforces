from collections import Counter
for _ in range(int(input())):
    x = int(input())
    ok = True
    check = Counter()
    for i in range(x):
        s = input()
        for c in s:
            check[c] += 1
    for elem in check.elements():
        if check[elem] % x:
            ok = False
            break
    print("YES" if ok else "NO")
