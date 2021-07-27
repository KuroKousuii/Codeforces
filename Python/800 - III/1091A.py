y, b, r = map(int, input().split())
if b >= r-1 and y >= r-2:
    print((r-1)*3)
elif r >= b+1 and y >= b-1:
    print(b*3)
else:
    print((y+1)*3)
