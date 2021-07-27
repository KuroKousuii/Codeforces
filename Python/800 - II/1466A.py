for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    s = set()
    for i in range(x-1):
        for j in range(i+1, x):
            s.add(abs(arr[i]-arr[j]))
    print(len(s))
