x, y = map(int, input().split())
first = [*map(str, input().split())]
last = [*map(str, input().split())]
for i in range(int(input())):
    check = int(input())-1
    print(f'{first[check%x]}{last[check%y]}')