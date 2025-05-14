
danh_sach_email = []

while True:
    try:
        ten = input("Nhập tên nhân viên (hoặc ENTER để kết thúc): ")

        if ten == "":
            break

        if not ten.isalnum():
            raise ValueError("Tên không được chứa ký tự đặc biệt!")

        email = ten + "@companyname.com"
        danh_sach_email.append(email)
        print("Tạo email:", email)

    except ValueError as e:
        print("Lỗi:", e)

print("\nDanh sách email đã tạo:")
for e in danh_sach_email:
    print(e)
