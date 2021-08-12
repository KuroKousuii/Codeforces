x, y, z = map(int, input().split())
if x < y:
    print('-' if x+z < y else '?')
elif x > y:
    print('+' if y+z < x else '?')
else:
    print(0 if z == 0 else '?')