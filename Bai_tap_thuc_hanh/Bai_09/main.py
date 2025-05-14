import qlyhanghoa as ql

# Nhập danh sách mặt hàng
ds = ql.nhap_danh_sach()

# In danh sách ban đầu
print("\n--- DANH SÁCH BAN ĐẦU ---")
ql.in_danh_sach(ds)

# Sắp xếp theo thuế giảm dần
ds_sap_xep = ql.sap_xep_theo_thue(ds)

# In danh sách sau sắp xếp
print("\n--- DANH SÁCH SAU KHI SẮP XẾP THEO THUẾ GIẢM DẦN ---")
ql.in_danh_sach(ds_sap_xep)

