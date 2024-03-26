Toan = float(input("nhap diem toan: "))
Ly = float(input("nhap diem ly: "))
Hoa = float(input("nhap diem hoa: "))
sum= Toan+Ly+Hoa

if sum>=15 and Toan>=4 and Ly>=4 and Hoa>=4:
    print("đậu")
    if Toan>=5 and Ly>=5 and Hoa>=5:
        print("học đều các môn")
    else:
        print("học chưa đều các môn")
else:
    print("không đậu")