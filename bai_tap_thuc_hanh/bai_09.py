import qlyhanghoa

ds = qlyhanghoa.nhap_danh_sach_hang_hoa()
qlyhanghoa.tinh_thanh_tien_va_thue(ds)
qlyhanghoa.in_danh_sach(ds, title="DANH SÁCH TRƯỚC KHI SẮP XẾP")
qlyhanghoa.sap_xep_theo_thue_giam_dan(ds)
qlyhanghoa.in_danh_sach(ds, title="DANH SÁCH SAU KHI SẮP XẾP THEO THUẾ GIẢM DẦN")