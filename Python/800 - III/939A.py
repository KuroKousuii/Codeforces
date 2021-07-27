x = int(input())
arr = [*map(int, input().split())]
new = [i-1 for i in arr]
for i in range(x):
    if new[new[new[i]]] == i:
        print("YES")
        exit(0)
print("NO")