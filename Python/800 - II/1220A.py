x = int(input())
s = input()
for _ in range(s.count('n')):
    print(1, end=" ")
for _ in range(s.count('z')):
    print(0, end=" ")
