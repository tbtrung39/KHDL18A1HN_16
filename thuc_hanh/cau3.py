
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

vi_tri_am_dau = next((i for i, x in enumerate(a) if x < 0), -1)
if vi_tri_am_dau != -1:
    print("Vị trí của phần tử âm đầu tiên trong danh sách là:", vi_tri_am_dau)
else:
    print("Danh sách không có số âm.")
