n = int(input("nhap n:"))
sum = int(0)
for i in range(1,n):
    if i%4==0 and i%5 !=0:
        sum+=i
print(sum)