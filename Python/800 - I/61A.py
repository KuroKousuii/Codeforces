import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
fin = ""
for i in range(len(s1)):
    fin += "1" if s1[i] != s2[i] else "0"
print(fin)
