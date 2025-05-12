def nhap_hang():
    ds_hang = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nMặt hàng {i+1}:")
        ma = input("  Mã hàng (4 ký tự): ")
        ten = input("  Tên hàng: ")
        dvt = input("  Đơn vị tính: ")
        dongia = float(input("  Đơn giá: "))
        soluong = int(input("  Số lượng: "))
        thanhtien = dongia * soluong
        thue = thanhtien * 0.1
        hang = {
            "ma": ma,
            "ten": ten,
            "dvt": dvt,
            "dongia": dongia,
            "soluong": soluong,
            "thanhtien": thanhtien,
            "thue": thue
        }
        ds_hang.append(hang)
    return ds_hang

def in_danh_sach(ds_hang):
    print("\n{:<6}{:<15}{:<10}{:<10}{:<10}{:<12}{:<10}".format("Mã", "Tên", "ĐVT", "Đơn giá", "S.lượng", "Thành tiền", "Thuế"))
    for hang in ds_hang:
        print("{:<6}{:<15}{:<10}{:<10.2f}{:<10}{:<12.2f}{:<10.2f}".format(
            hang["ma"], hang["ten"], hang["dvt"], hang["dongia"],
            hang["soluong"], hang["thanhtien"], hang["thue"]
        ))

def sap_xep_theo_thue(ds_hang):
    return sorted(ds_hang, key=lambda x: x["thue"])
