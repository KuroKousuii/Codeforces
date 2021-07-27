for _ in range(int(input())):
    sent = input()
    print("FILIPINO" if sent[-1] == 'o' else "JAPANESE" if sent[-1] == 'u' else "KOREAN")