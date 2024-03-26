def cong(x,y):
    return x+y
def tru(x,y):
    return x-y
def nhan(x,y):
    return x*y
def chia(x,y):
    if y!=0:
        return x/y
    else:
        return "khong the chia cho 0"
def sodu(x,y):
    if y != 0:
        return x % y
    else:
        return "khong the lay so du cho 0"
toan_hang_1 = float(input("Toán hạng 1: "))
toan_hang_2 = float(input("Toán hạng 2: "))
toan_tu = input("Toán tử: ")
if toan_tu == "+":
    print(toan_hang_1,"+",toan_hang_2,"=",cong(toan_hang_1,toan_hang_2))
if toan_tu == "-":
    print(toan_hang_1,"-",toan_hang_2,"=",tru(toan_hang_1,toan_hang_2))
if toan_tu == "*":
    print(toan_hang_1,"*",toan_hang_2,"=",nhan(toan_hang_1,toan_hang_2))
if toan_tu == "/":
    if toan_hang_2 == 0:
        print("khong the chia cho 0")
    else:
        print(toan_hang_1,"/",toan_hang_2,"=",chia(toan_hang_1,toan_hang_2))
if toan_tu == "%":
    if toan_hang_2 == 0:
        print("khong the lay so du cho 0")
    else:
        print(toan_hang_1,"%",toan_hang_2,"=",sodu(toan_hang_1,toan_hang_2))