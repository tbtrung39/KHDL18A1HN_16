a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
so_1 = a
so_2 = b
bcnn = a if a > b else b 

while True:
    if bcnn % a == 0 and bcnn % b == 0:
        break  
    bcnn += 1  
print(f"Bội chung nhỏ nhất của {so_1} và {so_2} là: {bcnn}")
