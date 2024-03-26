n = int(input("nhap n: "))
res = []
count = 0
sum = 0
for i in range(1,n+1):
    if (n%i==0):
        res.append(i)
        count+=1
        sum+=i
print(res)
print(count)
print(sum)