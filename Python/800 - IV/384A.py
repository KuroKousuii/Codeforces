x = int(input())
print((x*x+1)//2)
for i in range(x):
    for j in range(x):
        print('C' if (i+j) % 2 == 0 else '.', end="")
    print()
