x = int(input())
arr = [*map(int, input().split())]
total, now = 0, 0
for i in arr:
    if i == -1:
        if now == 0:
            total += 1
        else:
            now -= 1
    else:
        now += i
print(total)