num = int(input("Nhập số nguyên có 3 chữ số: "))
numbers = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
hundred = numbers[num // 100] + " trăm"
ten = numbers[(num // 10) % 10] + " mươi"
one = numbers[num % 10]
print(f"{hundred} {ten} {one}")