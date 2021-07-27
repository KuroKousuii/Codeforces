x = int(input())
one, two = 0, 0
for i in range(x):
    a, b = map(int, input().split())
    one += a > b
    two += b > a
print("Mishka" if one > two else "Chris" if two > one else "Friendship is magic!^^")
