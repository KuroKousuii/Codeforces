from collections import defaultdict
n, m = map(int, input().split())
check = defaultdict(int)
for i in range(n):
    arr = [*map(int, input().split())]
    for j in range(1, len(arr)):
        check[arr[j]] += 1
print("YES" if len(check) == m else "NO")