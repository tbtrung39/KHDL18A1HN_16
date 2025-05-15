def xu_ly_loi_nhap_du_lieu():
    while True:
        try:
            chuoi_nhap = input("nhập một kí tự a-z,A-Z: ")
            if not chuoi_nhap.isalpha():
                raise Exception('lỗi nhập kí tự')
            for i in range (len(chuoi_nhap)-1):
                if chuoi_nhap[i] == chuoi_nhap[i+1]:
                    raise Exception('lỗi nhập dữ liệu')
                for i in range (len(chuoi_nhap)-3):
                    if chuoi_nhap[i] == chuoi_nhap[i+1]== chuoi_nhap[i+2]== chuoi_nhap[i+3]:       
                        raise Exception('lỗi nhập lặp lại')
                if len(chuoi_nhap)>=5:
                    for i in (len(chuoi_nhap)-4):

                        if len(set(chuoi_nhap[i:i+5]))==1:
                           raise Exception('lỗi nhập trùng lặp')
                        print('chuỗi nhập hợp lệ',chuoi_nhap)
                        break
        except Exception as loi:
            print(loi)
            print('vui lòng nhập lại')
xu_ly_loi_nhap_du_lieu()
