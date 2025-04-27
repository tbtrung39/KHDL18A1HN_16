def tim_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_cac_so_truoc = tim_max(arr, n-1)
        return max(max_cac_so_truoc, arr[n-1])

arr = []
for i in range(3):
    so = int(input(f"Nhập số thứ {i+1}: "))
    arr.append(so)

ket_qua = tim_max(arr, len(arr))
print("Số lớn nhất là:", ket_qua)
