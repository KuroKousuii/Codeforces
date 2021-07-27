for _ in range(int(input())):
    x = int(input())
    mn = 10e9
    arr = [*map(int, input().split())]
    for i in range(x-1):
        for j in range(i+1, x):
            mn = min(abs(arr[i]-arr[j]), mn)
    print(mn)
