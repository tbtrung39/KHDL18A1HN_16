try:
    ten_tep_nguon = input("Nhập tên tập tin nguồn: ")
    tep_nguon = open(r"lab_12\Bai_04\input.txt", 'r')
    noi_dung = tep_nguon.read()
    ten_tep_dich = input("Nhập tên tập tin đích để ghi nội dung vào: ")
    try:
        tep_dich = open(r"lab_12\Bai_04\output.txt", 'w')
        tep_dich.write(noi_dung)
        print("Ghi dữ liệu thành công!")
    except IOError:
        print("Lỗi: Không thể ghi vào tập tin đích!")
    finally:
        try:
            tep_dich.close()
        except:
            pass

except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin nguồn!")
except IOError:
    print("Lỗi: Không thể đọc tập tin nguồn!")
finally:
    try:
        tep_nguon.close()
    except:
        pass