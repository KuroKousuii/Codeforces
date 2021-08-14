def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n, m = int(input()), 1
while isPrime(n*m+1):
    m += 1
print(m)