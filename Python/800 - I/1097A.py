sample = input()
check = [*map(str, input().split())]
for i in check:
    if i[0] == sample[0] or i[1] == sample[1]:
        print("YES")
        exit(0)
print("NO")