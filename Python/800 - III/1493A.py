for _ in range(int(input())):
    n, k = map(int, input().split())
    print(max(0, n-k)+k//2)
    for i in range(k+1, n+1, 1):
        print(i, end=" ")
    for i in range((k+1)//2, k, 1):
        print(i, end=" ")
    print()