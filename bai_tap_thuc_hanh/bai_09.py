numbers = list(map(int,input("Nhập các số nguyên , cách nhau bởi dấu cách:").split()))
assert all(num % 2 == 0 for num in numbers)
print("Tất cả các số đều là số chẵn")