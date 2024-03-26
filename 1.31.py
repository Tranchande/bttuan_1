x = float(input("nhap so km/h vuot toc do cho phep:"))
if x<=5:
    print("khong bi phat")
elif x<=10:
    print("phat 0.7 trieu")
elif x<=20:
    print("phat 2.5 trieu")
elif x<=35:
    print("phat 5.5 trieu")
else:
    print("phat 7.5 trieu")