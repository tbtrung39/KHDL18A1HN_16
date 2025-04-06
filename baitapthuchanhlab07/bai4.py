chieu_cao_str = "161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163 162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170"
chieu_cao_list = [int(h) for h in chieu_cao_str.split()]
so_sinh_vien = len(chieu_cao_list)
print(f"a. Số sinh viên trong nhóm là: {so_sinh_vien}")
tong_chieu_cao = sum(chieu_cao_list)
chieu_cao_trung_binh = tong_chieu_cao / so_sinh_vien
print(f"b. Chiều cao trung bình của các sinh viên trong nhóm là: {chieu_cao_trung_binh:.2f}")
so_sinh_vien_unique = len(set(chieu_cao_list))
print(f"(Kiểm tra) Số sinh viên duy nhất (theo chiều cao): {so_sinh_vien_unique}")
thong_ke_chieu_cao = {}
for chieu_cao in chieu_cao_list:
    thong_ke_chieu_cao[chieu_cao] = thong_ke_chieu_cao.get(chieu_cao, 0) + 1
print("(Thống kê chi tiết chiều cao):")
for chieu_cao, tan_suat in thong_ke_chieu_cao.items():
    print(f"- Chiều cao {chieu_cao}: {tan_suat} sinh viên")