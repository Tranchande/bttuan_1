n = float(input("nhap so Kwh dien dung: "))
tongtien = 0
if n>200:
    tongtien+= (n-200)*2500
    n=200
if n>150:
    tongtien+=(n-150)*2000
    n=150
if n>100:
    tongtien+=(n-100)*1200
    n=100
if n<=100:
    tongtien+= n*1000
print("tong tien phai tra la:",tongtien)