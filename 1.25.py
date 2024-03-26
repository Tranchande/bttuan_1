def namnhaun(n):
    if (n%4 == 0 and n%100!=0) or n%400==0:
        return True
    else:
        return False
a = int(input("nhap thang: "))
b = int(input("nhap nam: "))
if a==2 and namnhaun(b):
    print(29)
elif a==2 and not namnhaun(b):
    print(28)
elif a==4 or a==6 or a==9 or a==11:
    print(31)
else:
    print(30)