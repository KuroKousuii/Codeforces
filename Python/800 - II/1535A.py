for _ in range(int(input())):
    arr = [*map(int, input().split())]
    check = sorted(arr, reverse=True)
    adv1, adv2 = max(arr[0], arr[1]), max(arr[2], arr[3])
    if adv2 < adv1:
        adv1, adv2 = adv2, adv1
    # print(f'{adv1} {adv2}')
    print("YES" if adv1 == check[1] and adv2 == check[0] else "NO")
