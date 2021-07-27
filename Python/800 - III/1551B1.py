from collections import defaultdict
for _ in range(int(input())):
    s = input()
    total = 0
    check = defaultdict(int)
    for c in s:
        check[c] += 1
    for k,v in check.items():
        total += min(2, v)
    print(total//2)