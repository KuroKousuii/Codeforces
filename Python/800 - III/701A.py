x = int(input())
arr = [*map(int, input().split())]
ind = sorted([(count, value) for count, value in enumerate(arr)], key=lambda k: k[1])
for i in range(x//2):
    print(f'{ind[i][0]+1} {ind[x-i-1][0]+1}')
    