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
    if a==b and b==c:
        print("tam giac deu")
    elif (a**2 + b**2 == c**2) and (a==b or b==c or c == a):
        print("tam giac vuong can")
    elif  (a**2 + b**2 == c**2) and not (a==b or b==c or c == a):
        print("tam giac vuong")
    elif not (a**2 + b**2 == c**2) and (a==b or b==c or c == a):
        print("tam giac can")
    else:
        print("tam giac thuong")
else:
    print("khong la tam giac")