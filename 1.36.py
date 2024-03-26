def nganhang():
    a = input("nhap loai:")
    if a in('v','t'):
        if a == 't':
            tienlai = 0
            so_du_tt = int(input("nhap so du toi thieu: "))
            so_du_ct = int(input("nhap so du cuoi thang:"))
            if so_du_ct < so_du_tt:
                tienlai -=10
            else:
                tienlai=0.04*so_du_ct
        else:
            tienlai = 0
            so_du_tt = int(input("nhap so du toi thieu: "))
            so_du_ct = int(input("nhap so du cuoi thang:"))
            if so_du_ct < so_du_tt:
                tienlai -= 25
            else:
                if so_du_ct - so_du_tt >= 5000:
                    tienlai= so_du_ct*0.03
                else:
                    tienlai = so_du_ct*0.05
        return tienlai
    else:
        return 0

if __name__ == "__main__":
    a = nganhang()
    if a>0:
        print("tien lai la:",a)
    else:
        print("tien phai dong phat la:",-a)