x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
print("YES" if x <= a and x+y <= a+b and x+y+z <= a+b+c else "NO")

