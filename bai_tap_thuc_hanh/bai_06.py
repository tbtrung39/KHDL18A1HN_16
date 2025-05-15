def kiem_tra_username_hop_le(username):
    return username.isalnum()

def main():
    danh_sach_email = []
    ten_mien_cong_ty = "@companyname.com"

    while True:
        try:
            username = input("Nhập username của nhân viên (hoặc gõ 'thoat' để kết thúc): ")

            if username.lower() == 'thoat':
                break

            if not kiem_tra_username_hop_le(username):
                raise ValueError("Lỗi: Username chỉ được chứa chữ cái và chữ số, không được có dấu cách hoặc ký tự đặc biệt.")

            email = username + ten_mien_cong_ty
            danh_sach_email.append(email)
            print(f"Đã thêm email: {email}")

        except ValueError as loi:
            print(loi)

    print("\nDanh sách email nhân viên:")
    for email in danh_sach_email:
        print(email)

if __name__ == "__main__":
    main()