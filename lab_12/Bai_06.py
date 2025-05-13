def kiem_tra_username(username):
    if " " in username:
        raise ValueError("Lỗi: Username không được chứa dấu cách!")
    if not username.isalnum():
        raise ValueError("Lỗi: Username chỉ được chứa chữ cái và số!")
    return True
danh_sach_email = []
while True:
    try:
        str_username = input("Nhập username của nhân viên (hoặc nhập 'exit' để thoát): ")
        if str_username.lower() == 'exit':
            break
        if kiem_tra_username(str_username):
            email = str_username + "@companyname.com"
            danh_sach_email.append(email)
            print("Đã thêm email:", email)
    except ValueError as e:
        print(e)
print("\nDanh sách email đã nhập:")
for email in danh_sach_email:
    print("-", email)