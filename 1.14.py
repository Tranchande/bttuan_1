x = []
x.append(0)
x.append(1)
a = int(input("nhap so thu n: "))
for i in range(2,a+1):
    temp = x[i-2]+x[i-1]
    x.append(temp)
print(x[a])
