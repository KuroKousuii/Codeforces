for _ in range(int(input())):
    x, mx = int(input()), 0
    s = input()
    arr = [i for i in range(x) if s[i] == 'A']
    arr.append(x)
    for i in range(1, len(arr), 1):
        mx = max(arr[i]-arr[i-1]-1, mx)
    print(mx)