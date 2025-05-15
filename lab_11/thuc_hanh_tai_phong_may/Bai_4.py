# Hàm kiểm tra một số có phải là số nguyên tố không
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Mở tệp đầu vào để đọc các số
with open("thuc_hanh_tai_phong_may/f_in.dat", "r") as fin:
    cac_dong = fin.readlines()

# Mở tệp đầu ra để ghi kết quả
with open("thuc_hanh_tai_phong_may/f_out.dat", "w") as fout:
    for dong in cac_dong:
        n = int(dong.strip())
        uoc_nt = []

        for i in range(1, n + 1):
            if n % i == 0 and la_nguyen_to(i):
                uoc_nt.append(str(i))  # Ghi dưới dạng chuỗi để ghi vào tệp

        fout.write(" ".join(uoc_nt) + "\n")