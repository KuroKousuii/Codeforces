n, k = map(int, input().split())
arr = [*map(int, input().split())]
check, ind = set(), []
for i in range(n):
    if arr[i] not in check:
        ind.append(i+1)
        check.add(arr[i])
if len(check) < k:
    print("NO")
else:
    print("YES")
    for i in range(k):
        print(ind[i], end=" ")
