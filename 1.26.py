a = int(input("nhap so n: "))
def switchtoword(n):
    if n == 0:
        return "không"
    elif n == 1:
        return "một"
    elif n == 2:
        return "hai"
    elif n == 3:
        return "ba"
    elif n == 4:
        return "bốn"
    elif n == 5:
        return "năm"
    elif n == 6:
        return "sáu"
    elif n == 7:
        return "bảy"
    elif n == 8:
        return "tám"
    elif n == 9:
        return "chín"
print(switchtoword(a))
