from collections import defaultdict
for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    check, need = sorted(set(arr)), defaultdict(int)
    for i in arr:
        need[i] += 1
    for i in check:
        print(i, end=" ")
    for k, v in need.items():
        for i in range(v-1):
            print(k, end=" ")
    print()