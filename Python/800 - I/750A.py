x, y = map(int, input().split())
y = 240 - y
cur, step = 0, 0
while cur < y:
    cur += step*5
    if cur >= y:
        if cur > y:
            step -= 1
        break
    step += 1
print(min(step, x))
