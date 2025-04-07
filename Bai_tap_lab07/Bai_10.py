m = input("Nhập số tự nhiên m: ")
n = input("Nhập số tự nhiên n: ")

common_digits = set(m) & set(n)
total = sum(int(d) for d in common_digits)

print("Các chữ số chung:", common_digits)
print("Tổng các chữ số chung:", total)