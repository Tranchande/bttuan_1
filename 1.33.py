a = float(input("nhap a: "))
b = float(input("nhap b: "))
c = float(input("nhap c: "))
sapxep = sorted([a, b, c])
a = sapxep[0]
b = sapxep[1]
c = sapxep[2]
def tamgiac(x,y,z):
    if z<x+y:
        return True
    else:
        return False
if tamgiac(a,b,c):
   if  a ** 2 + b ** 2 == c ** 2:
       print("la 3 canh cua mot tam giac vuong")
else:
    print("khong la tam giac")