x, y = map(int, input().split())
row, col = set(), set()
for i in range(x):
    s = input()
    for j in range(y):
        if s[j] == 'S':
            row.add(i)
            col.add(j)
print(x*y-len(row)*len(col))