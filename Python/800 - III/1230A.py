arr = sorted([*map(int, input().split())])
print("YES" if arr[0]+arr[1]+arr[2] == arr[3] or arr[1]+arr[2] == arr[0]+arr[3] else "NO")