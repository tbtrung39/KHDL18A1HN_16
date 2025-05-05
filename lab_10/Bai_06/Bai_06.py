#Bước 2(Bài 6):
import doicoso2

input_string = input("Nhập vào một chuỗi ký tự: ")
filtered_string = doicoso2.loc_chuoi(input_string)
print("Chuỗi sau khi lọc:", filtered_string)

base = doicoso2.xac_dinh_co_so(filtered_string)
if base:
    print("Cơ số của chuỗi:", base)
    decimal_value = doicoso2.chuyen_doi_sang_co_so_10(filtered_string, base)
    if decimal_value:
        print("Giá trị ở cơ số 10:", decimal_value)
    else:
        print("Không thể chuyển đổi sang cơ số 10.")
else:
    print("Không xác định được cơ số.")