import qlyhanghoa

ds = qlyhanghoa.nhap_hang()

print("\n--- DANH SÁCH MẶT HÀNG BAN ĐẦU ---")
qlyhanghoa.in_danh_sach(ds)

ds_sx = qlyhanghoa.sap_xep_theo_thue(ds)
print("\n--- DANH SÁCH SAU KHI SẮP XẾP TĂNG DẦN THEO THUẾ ---")
qlyhanghoa.in_danh_sach(ds_sx)
