a, b, c = map(int, input().split())
if a < b:
    a, b = b, a
print(c*2+min(b+1, a)+b)
