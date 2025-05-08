with open("Bài_tập_thực_Hành/m_nums.txt", "r") as f:
    data1 = f.read()
    nums1 = set(map(int, data1.strip().split()))

with open("Bài_tập_thực_Hành/n_nums.txt", "r") as f:
    data2 = f.read()
    nums2 = set(map(int, data2.strip().split()))

common_nums = sorted(nums1 & nums2)  

with open("Bài_tập_thực_Hành/so_chung.txt", "w") as f:
    f.write(" ".join(map(str, common_nums)))

print("Các số chung có trong cả hai file là:")
with open("Bài_tập_thực_Hành/so_chung.txt", "r") as f:
    print(f.read()) 