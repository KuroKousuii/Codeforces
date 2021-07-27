x = int(input())
check = x % 4
if check == 0:
    print(f'{1} A')
elif check == 1:
    print(f'{0} A')
elif check == 2:
    print(f'{1} B')
else:
    print(f'{2} A')