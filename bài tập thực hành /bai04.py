try:
    input_file = input("Nhập tên tệp nguồn: ")
    output_file = input("Nhập tên tệp đích để lưu nội dung: ")

    with open(input_file, "r", encoding="utf-8") as f_in:
        data = f_in.read()

    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write(data)

    print(f"Đã ghi nội dung từ '{input_file}' sang '{output_file}'.")

except FileNotFoundError:
    print("Lỗi: Tệp nguồn không tồn tại.")
except PermissionError:
    print("Lỗi: Không có quyền ghi vào tệp đích.")
except IOError:
    print("Lỗi: Không thể đọc hoặc ghi tệp.")
except Exception as e:
    print("Lỗi không xác định:", e)