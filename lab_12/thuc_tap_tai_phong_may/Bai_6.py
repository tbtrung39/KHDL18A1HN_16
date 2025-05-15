def tao_email_danh_sach():
    import re  # Sử dụng để kiểm tra biểu thức chính quy

    danh_sach_email = []
    domain = "@companyname.com"

    while True:
        try:
            username = input("Nhập username nhân viên (gõ 'exit' để kết thúc): ")

            if username.lower() == 'exit':
                break

            # Kiểm tra không được để trống
            if not username.strip():
                raise ValueError("Lỗi: Username không được để trống!")

            # Kiểm tra dấu cách
            if " " in username:
                raise ValueError("Lỗi: Username không được chứa dấu cách!")

            # Kiểm tra username chỉ bao gồm chữ cái và số (sử dụng regex)
            if not re.match("^[a-zA-Z0-9]+$", username):
                raise ValueError("Lỗi: Username chỉ được chứa chữ cái và chữ số!")

            # Nếu hợp lệ, ghép email và thêm vào danh sách
            email = username + domain
            danh_sach_email.append(email)
            print(f"Đã thêm email: {email}\n")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

    # In danh sách email đã nhập
    print("\n Danh sách email nhân viên:")
    for email in danh_sach_email:
        print(f"- {email}")

# Gọi hàm
tao_email_danh_sach()