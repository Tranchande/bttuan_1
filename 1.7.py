n = int(input("nhap n: "))
res = ''
while n!=0:
    temp = str(n%2);
    res+= temp
    n=n//2
res = res[::-1]
print(res)