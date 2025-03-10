n = int(input("Nhap so nguyen duong n :"))
if n < 0:
    print("Vui long nhap lại")

S4=0
i = 4
while i <= n:
    S4 += i**2
    i += 1
print("S4=",S4)
 
S5=0
i = 1
while i <= n:
    S5 += (2*i+1)**3
    i+=1
print("S5=",S5)

S6=0
i = 1
while i <= n:
    S6 += (2*i)**4
    i+=1
print("S6=",S6)