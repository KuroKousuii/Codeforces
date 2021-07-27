x = int(input())
start, add, layer, total = 0, 1, 0, 0
while total+start+add <= x:
    start += add
    total += start
    layer += 1
    add += 1
print(layer)