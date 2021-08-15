for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    print(max(n-r, r-1)+max(m-c, c-1))