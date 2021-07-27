x, y = map(int, input().split())
for i in range(x):
    if i % 2 == 0:
        print('#'*y)
    elif i % 4 == 1:
        print('.'*(y-1)+'#')
    else:
        print('#'+'.'*(y-1))