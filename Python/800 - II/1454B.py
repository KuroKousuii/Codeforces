from collections import Counter
for _ in range(int(input())):
    x = int(input())
    ans = -1
    arr = [*map(int, input().split())]
    cnt = Counter(arr)
    for a, b in sorted(cnt.items()):
        if b == 1:
            ans = arr.index(a)+1
            break
    print(ans)

