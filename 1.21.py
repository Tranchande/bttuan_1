def so_nguyen(n):
    try:
        int(n)
        return True
    except:
        return False
def clock():
    hours = input("nhap gio: ")
    if so_nguyen(hours)==False or int(hours)<0 or int(hours)>24:
        print("nhap sai!!!!")
        return 0
    minutes = input("nhap phut: ")
    if so_nguyen(minutes) == False or int(minutes) < 0 or int(minutes) >60:
        print("nhap sai!!!!")
        return 0
    giay = input("nhap giay: ")
    if so_nguyen(giay) == False or int(giay) < 0 or int(giay) > 60:
        print("nhap sai!!!!")
        return 0
    print("du lieu dau vao dung")

if __name__== "__main__":
    clock()