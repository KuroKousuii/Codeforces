x = int(input())
arr = [*map(int, input().split())]
check, deck = set(), []
for i in range(len(arr)-1, -1, -1):
    if arr[i] not in check:
        check.add(arr[i])
        deck.append(arr[i])
print(len(deck))
for i in range(len(deck)-1, -1, -1):
    print(deck[i], end=" ")