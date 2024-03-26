heighs = []
while True:
    heigh = float(input('Nhap vao chieu cao: '))
    if heigh == 0:
        break
    heighs.append(heigh)
print("Hoc sinh dung dau danh sach la: ",max(heighs),"(m)")
print("Hoc sinh dung cuoi danh sach la:",min(heighs),"(m)")