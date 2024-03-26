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
def maytinh():
    print("MAY TINH DON GIAN")
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Dung chuong trinh")
    print("\n")
    while True:
        print("Lua chon cua ban la:", end=" ")
        a = input("")
        if a in ('1','2','3','4'):
            num1= float(input("nhap so dau: "))
            num2= float(input("nhap so thu hai: "))
        if a == '1':
            print("Ket qua la: ", num1, "+", num2,"=", end=' ')
            print(cong(num1,num2))
        if a == '2':
            print("Ket qua la: ", num1, "-", num2,"=", end=' ')
            print(tru(num1,num2))
        if a == '3':
            print("Ket qua la: ", num1, "*", num2,"=", end=' ')
            print(nhan(num1,num2))
        if a == '4':
            if num2 == 0:
                print("khong the chia")
            else:
                print("Ket qua la: ", num1, "/", num2,"=", end=' ')
                print(chia(num1,num2))
        if a == '0':
            break


if __name__== "__main__":
    maytinh()