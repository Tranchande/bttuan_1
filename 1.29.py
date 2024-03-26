n = int(input("nhap so km: "))
ans = 0
tmp = n
if n >= 6:
    ans += (n - 5) * 11
    n = 5
if n >= 2:
    ans += (n - 1) * 13.5
    n = 1
if n >= 1:
    ans += 15
if tmp >= 120:
    ans = ans * 90 / 100
print(ans)