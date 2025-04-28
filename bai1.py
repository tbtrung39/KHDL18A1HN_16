def tim_max(lst, n):
    if n == 1:
        return lst[0]
    else:
        max_cua_nho_hon = tim_max(lst, n - 1)
        if lst[n - 1] > max_cua_nho_hon:
            return lst[n - 1]
        else:
            return max_cua_nho_hon

# Nhập 3 số từ bàn phím
lst = []
for i in range(3):
    x = int(input(f"Nhập số thứ {i+1}: "))
    lst.append(x)

# Gọi hàm đệ qui tìm số lớn nhất
ket_qua = tim_max(lst, len(lst))
print("Số lớn nhất là:", ket_qua)
