arr = [*map(int, input().split())]
s = input()
total = 0
for c in s:
    total += arr[ord(c)-ord('0')-1]
print(total)