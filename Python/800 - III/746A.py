a = int(input())
b = int(input())
c = int(input())
step = 0
while step <= a and step*2 <= b and step*4 <= c:
    step += 1
print((step-(step > a or step*2 > b or step*4 > c))*7)
