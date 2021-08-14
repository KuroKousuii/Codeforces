for _ in range(int(input())):
    h, w = map(int, input().split())
    plate = []
    for i in range(h):
        if i == 0:
            plate.append("10"*(w//2)+"1"*(w % 2))
        elif i == h-1:
            nw = ""
            for j in range(w):
                if i % 2 == 0:
                    plate.append("10"*(w//2)+"1"*(w % 2))
                    break
                else:
                    if j < 2 or j >= w-2:
                        nw += "0"
                    else:
                        if j % 2 == 0:
                            nw += "1"
                        else:
                            nw += "0"
            if nw != "":
                plate.append(nw)
        elif i % 2 == 0:
            plate.append("1"+"0"*(w-2)+"1")
        else:
            plate.append("0"*w)
    for p in plate:
        print(f'{p}')
    print()
