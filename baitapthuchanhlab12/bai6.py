COMPANY_NAME = "companyname.com"
def kiem_tra_username(username):
    if ' ' in username:
        raise ValueError("Lỗi: Username không được chứa dấu cách.")
    for char in username:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
            raise ValueError("Lỗi: Username chỉ được chứa chữ cái và chữ số.")
    return True

def main():
    danh_sach_email = []
    while True:
        try:
            username = input("Vui lòng nhập username (hoặc 'done' để kết thúc): ")
            if username.lower() == 'done':
                break

            if kiem_tra_username(username):
                email = f"{username}@{COMPANY_NAME}"
                danh_sach_email.append(email)
                print(f"Đã thêm email: {email}")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

    print("\n--- Danh sách các địa chỉ email đã tạo ---")
    for email in danh_sach_email:
        print(email)

if __name__ == "__main__":
    main()