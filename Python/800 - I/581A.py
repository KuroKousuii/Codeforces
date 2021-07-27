n, k = map(int, input().split())
if n > k:
    n, k = k, n
print(f'{n} {(k-n)//2}')