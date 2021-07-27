for _ in range(int(input())):
    n, m, x = map(int, input().split())
    locate1, locate2 = n if x % n == 0 else x % n, (x+n-1)//n
    # print(f'{locate1} {locate2}')
    print((locate1-1)*m+locate2)
