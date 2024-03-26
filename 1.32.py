a =int(input("nhap n:"))
if a<0 or a>35:
    print("nhap sai!!!!<<nhap trong khoang tu 0 den 35>>>")
else:
    if a<=9:
        print(a)
    else:
        temp = 65-10+a
        print(chr(temp))