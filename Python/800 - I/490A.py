x = int(input())
team = [[], [], []]
for cnt, al in enumerate(map(int, input().split()), 1):
    team[al-1].append(cnt)
print(len([*zip(*team)]))
for i in [*zip(*team)]:
    for j in i:
        print(j, end=" ")
    print()
