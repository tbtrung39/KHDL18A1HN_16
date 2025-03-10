print("Nhập một ký tự: ")
n = ""
while n == "":  
    n = input()

for i in n:
    ascii_value = ord(i)
    print("Mã ASCII của", i, "là:", ascii_value)
    break  