# Tạo các ngoại lệ tùy chỉnh
class KyTuKhongHopLe(Exception):
    pass

class LoiNhapLieu(Exception):
    pass

class LoiNhapLapLai(Exception):
    pass

class LoiNhapTrungLap(Exception):
    pass

def kiem_tra_chuoi(s):
    if not s.isalpha():
        raise KyTuKhongHopLe("Lỗi ký tự !!!")
    
    # Kiểm tra 5 ký tự trùng nhau liên tiếp
    for i in range(len(s) - 4):
        if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
            raise LoiNhapTrungLap("Lỗi nhập trùng lặp !!!")
    
    # Kiểm tra 4 ký tự trùng nhau liên tiếp
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            raise LoiNhapLapLai("Lỗi nhập lặp lại !!!")
    
    # Kiểm tra 2 ký tự trùng nhau liên tiếp
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            raise LoiNhapLieu("Lỗi nhập liệu !!!")

while True:
    try:
        chuoi = input("Nhập chuỗi ký tự: ")
        kiem_tra_chuoi(chuoi)
        print("Nhập hợp lệ")
        break  # kết thúc vòng lặp nếu nhập đúng
    except KyTuKhongHopLe as e:
        print(e)
    except LoiNhapLieu as e:
        print(e)
    except LoiNhapLapLai as e:
        print(e)
    except LoiNhapTrungLap as e:
        print(e)
    except Exception as e:
        print("Lỗi không xác định:", e)