# Nhập số lần tung xúc xắc
n = int(input("Nhập số lần tung xúc xắc: "))

# Tính xác suất theo công thức P = 1 - (215/216)^n
xac_suat = 1 - (215 / 216) ** n

# In kết quả làm tròn đến 2 chữ số thập phân
print("Xác suất ít nhất một lần cả 3 xúc xắc ra 6 là:", round(xac_suat, 2))
