emails = []
while True:
    try:
        username = input("Nhập username (Enter để kết thúc): ")
        if username == "":
            break
        if " " in username or not username.isalnum():
            raise ValueError("Tên không hợp lệ.")
        email = username + "@companyname.com"
        emails.append(email)
        print("Email đã tạo:", email)
    except ValueError as e:
        print("Lỗi:", e)
