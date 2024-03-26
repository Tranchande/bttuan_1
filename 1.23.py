def square_number(x):
    a = int(x**(1/2))
    if a*a == x:
        return True
    else:
        return False
if __name__ == "__main__":
    a = int(input("nhap so a: "))
    if square_number(a):
        print(f"{a} la so chinh phuong")
    else:
        print(f"{a} khong la so chinh phuong")