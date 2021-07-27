from collections import defaultdict
x = int(input())
has = defaultdict(int)
arr = [*map(int, input().split())]
for i in arr:
    has[i] += 1
print(max(has.values()))

