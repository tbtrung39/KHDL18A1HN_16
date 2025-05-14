n = int(input("Nhập số sinh viên: "))

a = int(input("Số sinh viên thi C++: "))
ds_cpp = input("Nhập danh sách sinh viên C++ (cách nhau bằng khoảng trắng): ").split()
cpp = set()
for x in ds_cpp:
    cpp.add(int(x))

b = int(input("Số sinh viên thi Java: "))
ds_java = input("Nhập danh sách sinh viên Java: ").split()
java = set()
for x in ds_java:
    java.add(int(x))

c = int(input("Số sinh viên thi Python: "))
ds_python = input("Nhập danh sách sinh viên Python: ").split()
python = set()
for x in ds_python:
    python.add(int(x))

mot_ngon_ngu = (cpp ^ java ^ python) - (cpp & java) - (cpp & python) - (java & python)
hai_ngon_ngu = ((cpp & java) | (cpp & python) | (java & python)) - (cpp & java & python)
ba_ngon_ngu = cpp & java & python

print("Sinh viên chỉ thi 1 ngôn ngữ:", mot_ngon_ngu)
print("Sinh viên thi 2 ngôn ngữ:", hai_ngon_ngu)
print("Sinh viên thi cả 3 ngôn ngữ:", ba_ngon_ngu)