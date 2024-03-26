x = int(input("hay nhap vao so nguyen x: "))
list = []
list.append(x)
while True:
    if x%2 == 0:
        temp = int(x/2)
        x = temp
    else:
        temp = int(3*x +1)
        x = temp
    list.append(temp)
    if temp == 1:
        break
result = ",".join(map(str, list))
print(result)