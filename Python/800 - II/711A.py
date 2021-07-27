x = int(input())
seat = []
ok = False
for i in range(x):
    row = input()
    if row[0:2] == "OO" and not ok:
        row = "++"+row[2::]
        ok = True
    elif row[3:5] == "OO" and not ok:
        row = row[:3:]+"++"
        ok = True
    seat.append(row)
if not ok:
    print("NO")
else:
    print("YES")
    for r in seat:
        print(r)
