a = int(input("nhap so nguyen duong a: "))
a_1 = str(a)
dao_1 = a_1[::-1]
print(dao_1)
count_chan = 0
count_le = 0
while a!=0:
    temp = a%10
    if temp%2 == 0:
        count_chan+=1
    else:
        count_le+=1
    a= a//10
print("so chu so chan la: ",count_chan)
print("so chu so le la: ",count_le)