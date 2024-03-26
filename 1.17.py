import time
def get_minutes(seconds):
    return (seconds//60)
def get_seconds(seconds):
    return seconds%60
def clock():
    minute = int(input("nhap so phut: "))
    while True:
        seconds = int(input("nhap so giay: "))
        if seconds >= 60:
            print("nhap sai xin hay nhap lai!!!")
        else:
            break
    sum = minute*60 + seconds
    for i in range(sum,-1,-1):
        a = get_minutes(i)
        b = get_seconds(i)
        if a==0 and b==0:
            result = f"{a:02}:{b:02}"
            print(result,"Reng reng reng")
        elif a==0 and b<6:
            result = f"{a:02}:{b:02}"
            print(result, "Tich tac")
            time.sleep(1)
        else:
            result = f"{a:02}:{b:02}"
            print(result)
            time.sleep(1)
clock()
