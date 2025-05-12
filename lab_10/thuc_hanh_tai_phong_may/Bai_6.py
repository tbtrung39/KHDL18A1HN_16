# bai_6.py

import doicoso2

def main():
    s = input("Nhập vào chuỗi ký tự: ")
    
    da_loc = doicoso2.loc_ky_tu_hop_le(s)
    print(f"Chuỗi sau khi loại bỏ ký tự không hợp lệ: {da_loc}")

    co_so = doicoso2.xac_dinh_co_so(da_loc)
    if co_so == -1:
        print("Không xác định được cơ số của chuỗi.")
    else:
        print(f"Chuỗi thuộc cơ số: {co_so}")
        if co_so == 2:
            print(f"Giá trị cơ số 10: {doicoso2.co_so_2_sang_10(da_loc)}")
        elif co_so == 8:
            print(f"Giá trị cơ số 10: {doicoso2.co_so_8_sang_10(da_loc)}")
        elif co_so == 16:
            print(f"Giá trị cơ số 10: {doicoso2.co_so_16_sang_10(da_loc)}")

if __name__ == "__main__":
    main()