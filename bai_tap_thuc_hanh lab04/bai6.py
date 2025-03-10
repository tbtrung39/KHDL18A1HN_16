hang_don_vi = ["","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
hang_chuc = ["","muoi","hai muoi","ba muoi","bon muoi","nam muoi","sau muoi","bay muoi","tam muoi","chin muoi"]
n = int(input("nhap mot so (0-99)|"))
if n ==0:
    print("so ban vua nhap la: khong")
else:
    result = ""
    hang_chuc_digit = n // 10
    hang_don_vi_digit = n %10
    if hang_chuc_digit > 0:
        result += hang_chuc[hang_chuc_digit]
    if hang_don_vi_digit > 0:
        if hang_chuc_digit >0:
            result += " "
        result += hang_don_vi[hang_don_vi_digit]
    print(f"so ban vua nhap la: {result}")