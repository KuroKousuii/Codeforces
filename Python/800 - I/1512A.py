for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    after = sorted(arr)
    print(arr.index(max(arr))+1 if after[0] == after[1] else arr.index(min(arr))+1)

