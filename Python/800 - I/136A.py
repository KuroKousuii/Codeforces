x = int(input())
l = list(map(int, input().split()))
for i in range(x):
    print(l.index(i+1)+1, end=" ")
