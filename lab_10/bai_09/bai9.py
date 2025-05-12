import qlyhanghoa

ds = qlyhanghoa.nhap_ds_hang()
qlyhanghoa.tinh_thanh_tien_va_thue(ds)

qlyhanghoa.in_danh_sach(ds, "Danh sach truoc khi sap xep")

ds_sap_xep = qlyhanghoa.sap_xep_theo_thue_giam(ds)
qlyhanghoa.in_danh_sach(ds_sap_xep, "Danh sach sau khi sap xep giam dan theo thue")
