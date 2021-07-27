x = int(input())
if x % 2:
    print(-1)
else:
    for i in range(1, x+1):
        print(i+i%2-(i%2==0), end=" ")
        