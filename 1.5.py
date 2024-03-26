n = int(input("nhap n: "))
def is_prime(number):
    if n<1:
        return False
    for i in range (2,number):
        if number%i == 0:
            return False
    return True
for i in range(n,1,-1):
    if is_prime(i):
        print(i)
        break


