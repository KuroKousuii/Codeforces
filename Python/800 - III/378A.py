a, b = map(int, input().split())
cntf, cntd, cnts = 0, 0, 0
for i in range(1, 7, 1):
    cntf += abs(a-i) < abs(b-i)
    cntd += abs(a-i) == abs(b-i)
    cnts += abs(a-i) > abs(b-i)
print(f'{cntf} {cntd} {cnts}')