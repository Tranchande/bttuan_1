n = int(input("nhap n: "))
sum=0
fac=1
for i in range(1,n+1):
    fac=fac*i
    sum=sum+fac
print(sum)