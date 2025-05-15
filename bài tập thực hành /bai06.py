import re

def is_valid_username(username):
    return re.fullmatch(r"[A-Za-z0-9]+", username) is not None

email_list = []

while True:
    username = input("Nhập username (hoặc 'q' để thoát): ")
    if username.lower() == 'q':
        break
    try:
        if not is_valid_username(username):
            raise ValueError("Username không hợp lệ. Chỉ được chứa chữ và số, không có dấu cách.")
        email = username + "@companyname.com"
        email_list.append(email)
        print(f"Email đã tạo: {email}")
    except ValueError as ve:
        print("Lỗi:", ve)

print("\nDanh sách email đã nhập:")
for email in email_list:
    print(email)