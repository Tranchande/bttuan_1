
a = int(input("nhap a: "))
b = int(input("nhap b: "))
def UCLN(x,y):
    if y ==0:
        return x
    else:
        return UCLN(y,x%y)
print(UCLN(a,b))
print(a*b/UCLN(a,b))