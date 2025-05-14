# Cau 9
def doc_trong_luong_hanh_ly(passenger_id_to_find="3"):
    """
    Đọc thông tin trọng lượng hành lý cho một hành khách cụ thể từ file WEIGHT.OUT.txt.

    Args:
        passenger_id_to_find (str): ID của hành khách cần tìm.
    """
    try:
        found_passenger = False
        with open("PASSENGERS.IN.txt", "r", encoding="utf-8") as file_in:
            for line in file_in:
                if passenger_id_to_find in line.split():  
                    found_passenger = True
                    print(f"Đã tìm thấy ID '{passenger_id_to_find}' trong file PASSENGERS.IN.txt.")
                    break
            if not found_passenger:
                print(f"Không tìm thấy ID '{passenger_id_to_find}' trong file PASSENGERS.IN.txt.")
                return
        weights = []
        with open("WEIGHT.OUT.txt", "r", encoding="utf-8") as file_out:
            for line in file_out:
                try:
                    weight = float(line.strip())
                    weights.append(weight)
                except ValueError:
                    print(f"Cảnh báo: Dòng không hợp lệ trong WEIGHT.OUT.txt: {line.strip()}")
        if weights:
            print(f"Trọng lượng hành lý tìm thấy trong WEIGHT.OUT.txt:")
            for weight in weights:
                print(f"- {weight} kg")
        else:
            print("Không có thông tin trọng lượng hành lý trong file WEIGHT.OUT.txt.")
    except FileNotFoundError as e:
        print(f"Lỗi: Không tìm thấy file: {e.filename}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
doc_trong_luong_hanh_ly()