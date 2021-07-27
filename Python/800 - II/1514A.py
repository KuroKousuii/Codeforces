import math
for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    check = [i for i in arr if int(math.sqrt(i))**2 == i]
    print("YES" if len(check) != x else "NO")