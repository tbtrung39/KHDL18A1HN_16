def kt_username(username):
    return username.isalnum()

email_list = []

while True:
    try:
        username = input("Nhập username nhân viên (hoặc 'q' để kết thúc): ")
        if username == 'q':
            break
        if not kt_username(username):
            raise ValueError("Lỗi")
        email = username + "@companyname.com"
        email_list.append(email)
        print(f"Đã thêm: {email}")

    except ValueError as v:
        print(v)
print("\nDanh sách email nhân viên:")
for e in email_list:
    print(e)