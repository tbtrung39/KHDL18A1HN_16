tu_so = float(input("Nhập tử số: "))  
mau_so = float(input("Nhập mẫu số: "))   
while mau_so == 0:  
    print("Mẫu số không được bằng 0! Vui lòng nhập lại.")  
    mau_so = float(input("Nhập mẫu số: "))  

print(f"Phân số bạn đã nhập là: {tu_so}/{mau_so}")  