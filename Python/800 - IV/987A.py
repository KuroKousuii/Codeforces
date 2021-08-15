from collections import defaultdict
x = int(input())
stone = defaultdict(str)
stone["red"] = "Reality"
stone["yellow"] = "Mind"
stone["orange"] = "Soul"
stone["blue"] = "Space"
stone["green"] = "Time"
stone["purple"] = "Power"
for _ in range(x):
    s = input()
    stone[s] = ""
print(6-x)
for k in stone.keys():
    if stone[k] != "":
        print(stone[k])
