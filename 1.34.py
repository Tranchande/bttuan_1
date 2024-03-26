x = float(input("nhap a: "))
y = float(input("nhap b: "))
z = float(input("nhap c: "))
import math
def giaiphuongtrinhbac2(a,b,c):
    if a == 0:
        if b == 0 and c== 0:
            print("phuong trinh vo so nghiem")
        if b == 0 and c!=0:
            print("phuong trinh vo nghiem")
        if b!=0:
            print("phuong trinh co 1 no la:",-c/b)
    else:
        if b**2 - 4*a*c < 0:
            print("phuong trinh vo nghiem")
        elif b**2 - 4*a*c ==0:
            print("phuong trinh co 1 nghiem kep la:",-b/(2*a))
        else:
            temp= math.sqrt(b**2 - 4*a*c)
            k= round((-b+temp)/(2*a),5)
            j= round((-b-temp)/(2*a),5)
            print("phuong trinh co 2 nghiem la:",k,",",j)
giaiphuongtrinhbac2(x,y,z)