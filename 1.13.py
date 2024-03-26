x= int(input("nhap dan so thanh pho A: "))
y = int(input("nhap dan so thanh pho B: "))
a= int(input("nhap ti le tang truong A:"))
b = int(input("nhap ti le tang truong B:"))
count= 0
while x<y:
    x=x*(1+a/100)
    y=y*(1+b/100)
    count+=1
print(count)

