#cach1
n=int(input("Nhap so tu nhien n: "))
binary=""
if n==0:
    binary=="0"
else:
    while n>0:
        binary=str(n%2) + binary
        n//=2
print("So nhi phan:",binary)

#cach2
n=int(input("Nhap so tu nhien n: "))
snp=bin(n)[2:]
print("So nhi phan:",snp)