for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > n//2-(n % 2 == 0):
        print(-1)
    else:
        peak, start = n, 1
        for i in range(k):
            print(f'{start} {peak}', end=" ")
            start += 1
            peak -= 1
        for i in range(n-k*2):
            print(start, end=" ")
            start += 1
        print()