for _ in range(int(input())):
    x = int(input())
    s = input()
    arr = [s[:4], s[:3]+s[-1:], s[:2]+s[-2:], s[:1]+s[-3:], s[-4:]]
    # print(*arr)
    print("YES" if "2020" in arr else "NO")
