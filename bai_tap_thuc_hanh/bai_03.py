try:
    file_name = input("Nhập tên tệp cần đọc: ")

    with open(file_name, "r", encoding="utf-8") as f_in:
        content = f_in.read()

    with open("bai_tap_thuc_hanh\copy.dat", "w", encoding="utf-8") as f_out:
        f_out.write(content)

    print("Đã sao chép nội dung sang copy.dat.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy tệp.")
except Exception as e:
    print("Đã xảy ra lỗi:", e)