
import os

try:
    ten_tap_tin = input("Nhập tên tập tin cần kiểm tra: ")
    if not os.path.exists(ten_tap_tin):
        raise FileNotFoundError("Tập tin không tồn tại!")
    else:
        print("Tập tin tồn tại. Nội dung sẽ được sao chép sang copy.dat")
        with open(ten_tap_tin, 'r', encoding='utf-8') as f:
            du_lieu = f.read()
        with open('copy.dat', 'w', encoding='utf-8') as f:
            f.write(du_lieu)
        print("Đã sao chép xong.")
except FileNotFoundError as e:
    print("Lỗi:", e)
