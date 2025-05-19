import doicoso2

def main():
    print("--- Chương trình chuyển đổi cơ số (0-9, A-F) ---")
    chuoi_so = doicoso2.nhap_chuoi_so_hex()
    co_so = doicoso2.xac_dinh_co_so(chuoi_so)

    if co_so:
        print(f"Chuỗi '{chuoi_so}' có thể là biểu diễn ở cơ số {co_so}.")

        decimal_tu_nhiphan = doicoso2.sang_decimal(chuoi_so, 2)
        if co_so <= 2 and decimal_tu_nhiphan is not None:
            print(f"Chuyển từ cơ số 2 sang 10: {decimal_tu_nhiphan}")
        elif co_so > 2:
            print("Chuỗi không phải là số nhị phân hợp lệ.")

        decimal_tu_batphan = doicoso2.sang_decimal(chuoi_so, 8)
        if co_so <= 8 and decimal_tu_batphan is not None:
            print(f"Chuyển từ cơ số 8 sang 10: {decimal_tu_batphan}")
        elif co_so > 8:
            print("Chuỗi không phải là số bát phân hợp lệ.")

        decimal_tu_thaplucphan = doicoso2.sang_decimal(chuoi_so, 16)
        if decimal_tu_thaplucphan is not None:
            print(f"Chuyển từ cơ số 16 sang 10: {decimal_tu_thaplucphan}")

    else:
        print("Không thể xác định cơ số hợp lệ cho chuỗi đã nhập.")

if __name__ == "__main__":
    main()