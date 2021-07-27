a, b = map(int, input().split())
cnt = 0
for _ in range(a):
    sign, num = input().split()
    nnum = int(num)
    if sign == "+":
        b += nnum
    else:
        if nnum > b:
            cnt += 1
        else:
            b -= nnum
    # print(b)
print(f'{b} {cnt}')
