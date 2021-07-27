from collections import defaultdict
x = int(input())
arr = [*map(int, input().split())]
check = defaultdict(int)
for i in range(x):
    if i % 3 == 0:
        check["chest"] += arr[i]
    elif i % 3 == 1:
        check["biceps"] += arr[i]
    else:
        check["back"] += arr[i]
print(max(check, key=check.get))

