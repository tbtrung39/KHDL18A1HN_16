def is_valid_username(username):
    if ' ' in username:
        raise ValueError("Lỗi: Username không được chứa dấu cách.")
    if not username.isalnum():
        raise ValueError("Lỗi: Username chỉ được chứa chữ cái và số.")
    return True

def main():
    danh_sach_email = []
    while True:
        try:
            username = input("Nhập username (hoặc gõ 'exit' để thoát): ").strip()
            if username.lower() == 'exit':
                break

            if is_valid_username(username):
                email = username + "@companyname.com"
                danh_sach_email.append(email)
                print(f"Email đã tạo: {email}")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

    print("\nDanh sách email nhân viên:")
    for email in danh_sach_email:
        print(email)

main()