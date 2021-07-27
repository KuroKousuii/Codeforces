sm = 0
name = ['I', 'C', 'T', 'D', 'O']
corr = [20, 6, 4, 12, 8]
for _ in range(int(input())):
    s = input()
    sm += corr[name.index(s[0])]
print(sm)