def cal(col, row):
    if col == 1 or row == 1:
        return 1
    return cal(col-1, row)+cal(col, row-1)


x = int(input())
print(cal(x, x))
