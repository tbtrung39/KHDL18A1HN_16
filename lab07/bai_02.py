numbers = []

while True:
    n = input("Nhap so tu nhien, nhap q de dung: ")
    if n == "q":
        break
    if n.isdigit(): 
        numbers.append(int(n))
    else:
        print("Vui long nhap so tu nhien hoac 'q'.")
A = set(numbers)

print("Danh sach numbers: ", numbers)
print("Tap hop A: ", A)