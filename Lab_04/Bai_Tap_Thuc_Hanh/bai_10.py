chu_so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
num=input("nhập số:")
while not num.isdigit():
    print("Vui lòng nhập sô nguyên dương.")
    num = input("Nhập số:")

i = 0
ket_qua = " "
while i < len(num):
    so= int(num[i])
    ket_qua+= chu_so[so] + " "
    i+=1
print("Kết quả:",ket_qua)