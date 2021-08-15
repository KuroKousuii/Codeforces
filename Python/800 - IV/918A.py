x = int(input())
first, second, third = 1, 2, 3
for i in range(x):
    if i > third:
        first = second
        second = third
        third = first + second
    print('O' if i == first-1 or i == second-1 or i == third-1 else 'o', end="")
