for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    check = sum(arr)+arr.count(0)
    print(arr.count(0)+(check == 0))
